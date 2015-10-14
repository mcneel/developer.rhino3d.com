---
layout: bootstrap
---

# MessageBox

Displays a message box. A message box contains a message and
        title, plus any combination of predefined icons and push buttons.
        

### Parameters:

- ***message*** = A prompt or message.
- ***buttons[opt]*** = buttons and icon to display. Can be a combination of the
  following flags. If omitted, an OK button and no icon is displayed
  0      Display OK button only.
  1      Display OK and Cancel buttons.
  2      Display Abort, Retry, and Ignore buttons.
  3      Display Yes, No, and Cancel buttons.
  4      Display Yes and No buttons.
  5      Display Retry and Cancel buttons.
  16     Display Critical Message icon.
  32     Display Warning Query icon.
  48     Display Warning Message icon.
  64     Display Information Message icon.
  0      First button is the default.
  256    Second button is the default.
  512    Third button is the default.
  768    Fourth button is the default.
  0      Application modal. The user must respond to the message box
         before continuing work in the current application.
  4096   System modal. The user must respond to the message box
         before continuing work in any application.
- ***title[opt]*** = the dialog box title
        

### Returns:


A number indicating which button was clicked:
  1      OK button was clicked.
  2      Cancel button was clicked.
  3      Abort button was clicked.
  4      Retry button was clicked.
  5      Ignore button was clicked.
  6      Yes button was clicked.
  7      No button was clicked.
        
