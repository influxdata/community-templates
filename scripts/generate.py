#!/usr/bin/env python3

import os
import pathlib

home_dir = pathlib.Path(__file__).resolve().parent.parent

print("----------------------------------------\nWelcome to the InfluxData Community Template Generator!")
print("This program will guide you through the process of creating a new Community Template.\n\n")

####### First Prompt: project name ###########
project_name = input("What is your project's name? (Leave blank to use 'new_project')\n")

if not project_name:
  project_name = 'new_project'

project_dir = "{0}/{1}".format(home_dir, project_name)
if not os.path.exists(project_dir):
  os.mkdir(project_dir)
  print("Creating a directory in %s\n" %(project_dir))
else:
  print("\nDirectory %s already exists, creating manifest in it.\n" %(project_dir))

manifest_file = open(project_dir + '/generated_manifest.json', 'w')
file_contents = '''
{{
  "project-name": "{project_name}"'''

file_contents = file_contents.format(project_name = project_name)

####### Second Prompt: templates
input_templates = []
print("Please list the locations of your templates to install, Q to exit.")
print("Template locations should be paths relative to %s" %(project_dir))

while True:
  path = input('>')
  if path == 'Q' or path == 'q':
    break
  if path:
    input_templates.append(path)

resource_list = '['
resource_list +=  ', '.join('"{0}"'.format(r) for r in input_templates)

resource_contents = '''
  {file_contents},
  "templates": {resource_list}'''

resource_list += ']'
file_contents = resource_contents.format(file_contents = file_contents, resource_list = resource_list)

####### Cleanup
file_contents += '\n}'
file_contents = file_contents.strip()
print(file_contents)

manifest_file.write(file_contents)
manifest_file.close()

