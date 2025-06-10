def run_path(path_name, init_globals=None, run_name=None):
    """Execute code located at the specified filesystem location.

       path_name -- filesystem location of a Python script, zipfile,
       or directory containing a top level __main__.py script.

       Optional arguments:
       init_globals -- dictionary used to pre-populate the module's
       globals dictionary before the code is executed.

       run_name -- if not None, this will be used to set __name__;
       otherwise, '<run_path>' will be used for __name__.

       Returns the resulting module globals dictionary.
    """
    # ...existing code...