import sublime, sublime_plugin

class ErbTagsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if region.empty():
        self.view.replace(edit, region, "<%=  %>")
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(region.begin()+4, region.begin()+4))
      else:
        self.view.insert(edit, region.end(), " %>")
        self.view.insert(edit, region.begin(), "<%= ")
