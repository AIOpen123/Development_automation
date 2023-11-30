import gradio as gr
from calculator import calc_code
from chatgpt import chat_completion
import base64


choice_dict = {
"Comments": "Add comments for in the following Code in proper way", 
"Documentation": "Create a documentation for the below code", 
"Unit Tests": "write three unit tests for this function using xtest", 
"Explanation": "Explain what this code does", 
"Auto Completion": "Complete the following incomplete function", 
"Convert to C#": "Convert the following code into C#",
# "Create User Stories": "Create user stories for below use",
"Create User Stories": "Generate user stories for a from the perspective of Bussiness analyst or data analyst in a proffessional way. add acceptence criteria and tasks also ",
"Code Review": "Review the code below and provide feedback on how to improve it"
}

logo_url = r"C:\Users\rahulr6\Desktop\code review\kpmg.png"

def process_input(dropdown_selection, user_input):
    response =  chat_completion(f"{choice_dict.get(str(dropdown_selection))} \n --- \n {user_input}")
    return response

try:
    with open(logo_url, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
except:
    pass

iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Dropdown(
        choices=["Create User Stories", "Comments", "Unit Tests", "Documentation", "Explanation", "Auto Completion", "Convert to C#", "Code Review"],
        label="Choose an option",          
        ),
        gr.Textbox(label="Enter Input code")
    ],
    outputs=gr.Textbox(label="Response"),
    live=False,  
    title= f"<div style='text-align: center;'><img src='data:image/png;base64,{encoded_image}' alt='Logo' style='max-width: 150px; margin: 0 auto;'> CodeGaurd",
    thumbnail = logo_url,
    description="<div style='background-color: #3498db; padding: 10px;text-align: center'><h2 style='color: white;'>Empowering Effortless Application Building</h2></div>",
    allow_flagging = "never", 
    css = "footer{visibility:hidden}"
)   
iface.launch(show_api = False)