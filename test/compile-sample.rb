#
# compile-sample.rb
# ~~~~~~~~~~~~~~~~~
#

_version = "0.0.4"

# get filenames from commandline, e.g. ruby compile_sample.rb meshvolume.md addtext.md

if ARGV.count < 1
  puts "compile-sample.rb (#{_version})\n\n"
  puts "USAGE: ruby compile_sample.rb meshvolume.md addtext.md"
  puts "       ruby compile_sample.rb rhinocommon/*.md"
  exit
end

# define some handy string formatting
class String
  def black;          "\033[30m#{self}\033[0m" end
  def red;            "\033[31m#{self}\033[0m" end
  def green;          "\033[32m#{self}\033[0m" end
  def yellow;          "\033[33m#{self}\033[0m" end
  def magenta;        "\033[35m#{self}\033[0m" end
  def cyan;           "\033[36m#{self}\033[0m" end
  def grey;           "\033[37m#{self}\033[0m" end
  def success;        "\u2713 ".encode('utf-8') + self end
  def failure;        "\u2717 ".encode('utf-8') + self end
  def wut;        "\u271D ".encode('utf-8') + self end
end


files = ARGV
state = [] # record state of each test
skip_count = 0
t1 = Time.now

files.each do |filename|
  t11 = Time.now
  # check if markdown
  if File.directory?(filename)
    puts "#{filename} is a folder. I only eat files!".wut
    skip_count += 1
    next
  end
  unless filename.end_with? ".md"
    puts "#{filename} is not a markdown file!".wut
    skip_count += 1
    next
  end

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
  preamble << 'using Rhino.Collections;'
  preamble << 'using Rhino.Commands;'
  preamble << 'using Rhino.DocObjects;'
  preamble << 'using Rhino.Display;'
  preamble << 'using Rhino.Geometry;'
  preamble << 'using Rhino.Geometry.Collections;'
  preamble << 'using Rhino.Geometry.Intersect;'
  preamble << 'using Rhino.Geometry.Morphs;'
  preamble << 'using Rhino.Input;'
  preamble << 'using Rhino.Input.Custom;'
  preamble << 'using Rhino.UI;'
  preamble << 'using Rhino.UI.Gumball;'
  preamble << 'using System.Runtime.InteropServices;'
  preamble << ''

  # write to file
  File.open(filename + '.cs', 'w') do |file|
    preamble.each { |line| file.puts(line) }
    file.puts("class TestCompileWrapperClass\n\{") # wrap sample in a class, in case it is not already
    code.each { |line| file.puts(line) }
    file.puts("\}") # end wrapper class
  end

  # compile against rhinocommon and throw a wobbly if there's an error
  # note: rhinocommon dll must be in same dir
  # > nuget install RhinoCommon -source https://pyget.herokuapp.com/
  # > cp RhinoCommon*/lib/RhinoCommon.dll .
  output = `mcs #{filename}.cs -pkg:dotnet -r:RhinoCommon.dll -t:library 2>&1`
  delta = ((Time.now - t11) * 1000).round()
  unless $?.success?
    # print output
    output.split("\n").each do |line|
      puts "    " + line.grey # indent
    end
    # TODO last line is unnecessary (e.g. Compilation failed: 2 error(s), 0 warnings)
    puts "Could not compile #{filename} (#{delta} ms)".failure.red
    state << false
  else
    # TODO show warnings
    puts "Successfully compiled #{filename}  (#{delta} ms)".success.green
    state << true
  end
end

t2 = Time.now

# tally up the passes and fails
counts = Hash[true => 0, false => 0]
state.each { |s| counts[s] += 1 }

puts "\nFinished in %.2f seconds" % (t2 - t1)
skip_count = ARGV.count - state.count
puts "#{counts[true]}/#{state.count} samples compiled successfully (#{skip_count} skipped)".yellow

if counts[false] > 0 then exit 1 end
