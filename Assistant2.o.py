import wx
import wikipedia
import wolframalpha
import pyttsx3
engine=pyttsx3.init()
engine.say('welcome')
engine.runAndWait()
class MyFrame(wx.Frame):
    def __init__(self):
        engine=pyttsx3.init()
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Vk")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="I'm your Digital Assitant, How can i help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolframalpha

            app_id = "39H46W-4WQ6VGKK4X"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print(answer)
            engine.say('The answer is '+answer )
            engine.runAndWait()
        except:
            #wikipedia
            cutting_words=input.split()
            input=''.join(cutting_words[2:])
            engine.say('searched for '+input )
            engine.runAndWait()
            print(wikipedia.summary(input))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
