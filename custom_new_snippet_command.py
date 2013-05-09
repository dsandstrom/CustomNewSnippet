import sublime, sublime_plugin
import os


class CustomNewSnippetCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
          os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'sublime-snippet')
        v.set_syntax_file('Packages/XML/XML.tmLanguage')

        template = """<snippet>
  <content><![CDATA[
Hello, \${1:this} is a \${2:snippet}.
]]></content>
  <tabTrigger>hello</tabTrigger>
  <scope>source.python</scope>
  <description>snippet</description>
</snippet>
"""
        v.run_command("insert_snippet", {"contents": template})
