# open-in-vs-code 

Run "open_cmd" to add the command to the context menu.

If you want to delete, use "remove.exe".

In case of failure:

1) Press the Win + R keys on your keyboard at the same time to open the Run window.

2) Type "regedit" and press Enter to open the Registry Editor.

3)In the Registry Editor navigate to the following path:
HKEY_CLASSES_ROOT\Directory\Background\shell

4)In this section find the "OpenVsCode" key and right click on it.

5)Select "Delete" from the context menu.

6) Confirm key deletion.
