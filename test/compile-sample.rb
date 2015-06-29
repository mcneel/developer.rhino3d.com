# get filename from commandline, e.g. ruby compile_sample.rb meshvolume.md
filename = ARGV[0]

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
# rhinocommon dll must be in same dir
# > nuget install RhinoCommon -source https://pyget.herokuapp.com/
# > cp RhinoCommon*/lib/RhinoCommon.dll .
exit_code = system("mcs #{filename}.cs -r:RhinoCommon.dll -t:library")
raise "whoops" unless exit_code
