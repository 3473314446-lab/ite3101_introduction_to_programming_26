def shut_down(s:str)->str:
    return s
if yes():
    speak( "Shutting down")
elif no():
    speak("Shutdown aborted")
else:
    shut_down("sorry")