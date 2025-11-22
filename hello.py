import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# demo.launch(server_name="0.0.0.0",share=True, server_port= 7860)
demo.launch(server_name="0.0.0.0", server_port= 7860)

# http://localhost:7860 --> run on local host it will work on local environment unless share = True is provided
# for working may need to install from https://www.gyan.dev/ffmpeg/builds/ and add environment c:\ffmpeg\bin