# kn5-compatible-fbx_exporter-for-blender

A plugin for [Blender](https://www.blender.org/) that adds a tweaked fbx exporter to preserve the import file structure presumably from Autodesk softwares.

Blender has it's own indexing system that adds .001, 002 etc. to various objects and empties to give them unique names.

This custom exporter removes .001 to .099 from the names of your object and texture before exporting into .fbx files. 
