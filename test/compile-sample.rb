# get filenames from commandline, e.g. ruby compile_sample.rb meshvolume.md addtext.md
files = []
ARGV.each do |name|
  if File.directory?(name)
    puts name + ' is a folder. I only eat files!'
    exit
  else
    files << name
  end
end

state = [] # record state of each test

files.each do |filename|
  # extract cs code block from markdown
  code = []
  File.open(filename, 'r') do |file|
    in_code = false
    while (line = file.gets)
      if (not in_code) && line.start_with?('```cs')
        in_code = true
        next
      end
      if in_code
        unless line.start_with?('```')
          code << line
        else
          in_code = false
          break
        end
      end
    end
  end

  # preamble, using statements, etc.
  # TODO: complete (see cs script editor in gh)
  preamble = []
  preamble << 'using System;'
  preamble << 'using System.Collections.Generic;'
  preamble << 'using System.Drawing;'
  preamble << 'using System.Linq;'
  preamble << 'using System.Text;'
  preamble << 'using System.Threading;'
  preamble << 'using System.Threading.Tasks;'
  preamble << 'using Rhino;'
  preamble << 'using Rhino.Commands;'
  preamble << 'using Rhino.DocObjects;'
  preamble << 'using Rhino.Geometry;'
  preamble << 'using Rhino.Input.Custom;'
  preamble << ''

  # write to file
  File.open(filename + '.cs', 'w') do |file|
    preamble.each { |line| file.puts(line) }
    code.each { |line| file.puts(line) }
  end

  # compile against rhinocommon and throw a wobbly if there's an error
  # note: rhinocommon dll must be in same dir
  # > nuget install RhinoCommon -source https://pyget.herokuapp.com/
  # > cp RhinoCommon*/lib/RhinoCommon.dll .
  output = `mcs #{filename}.cs -pkg:dotnet -r:RhinoCommon.dll -t:library 2>&1`
  unless $?.success?
    output.split("\n").each do |line|
      puts "    \033[37m%s\033[0m" % line # print line in grey with indent
    end
    puts "\u2717".encode('utf-8') + ' Could not compile ' + filename
    state << false
  else
    puts "\u2713".encode('utf-8') + ' Successfully compiled ' + filename
    state << true
  end
end

# tally up the passes and fails
counts = Hash[true => 0, false => 0]
state.each { |s| counts[s] += 1 }

puts "\n%d/%d samples compiled successfully" % [counts[true], state.count]

if counts[false] > 0 then exit 1 end
