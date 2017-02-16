"""
The Pirates of Silicon Valley file contains an encoding
error. Run the program to find the error and manually look
in the file to find out what the problem is.

filename = "pirates_of_silicon_valley.srt"
"""
import pprint

# filename = "small_subtitles.srt"
filename = "pirates_of_silicon_valley.srt"
my_file = open(filename,encoding = "ISO-8859-1")

count = 0
js_string = "var SUBTITLES = [\n"
js_string_end = "];"

for line in my_file:
    line = line.strip()
    if "\"" in line:
        line = line.replace('"', '\\"')

    if len(line) == 0:
        if count == 3:
            js_string += '\t\tline2: "' + line + '"\n'
        count = 0
        js_string += '\t},\n'
    else:
        if count == 0:
            js_string += '\t{\n'
            count += 1
        elif count == 1:
            js_string += '\t\tduration: "' + line + '",\n'
            count += 1
        elif count == 2:
            js_string += '\t\tline1: "' + line + '",\n'
            count += 1
        elif count == 3:
            js_string += '\t\tline2: "' + line + '"\n'
            count += 1

if count == 3:
    js_string += '\t\tline2: "' + line + '"\n'
js_string += '\t}'
js_string += js_string_end

print(js_string)

js_file = open("pirates_of_silicon_valley.js", "w")
js_file.write(js_string)
js_file.close()
