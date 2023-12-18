# Display an updating digital clock in all viewports
import rhinoscriptsyntax as rs
import datetime

def viewportclock():
    now = datetime.datetime.now()
    textobject_id = rs.AddText(now, (0,0,0), 20)
    if textobject_id is None: return

    while True:
        rs.Sleep(1000)
        now = datetime.datetime.now()
        rs.TextObjectText(textobject_id, now)


if __name__=="__main__":
    viewportclock()