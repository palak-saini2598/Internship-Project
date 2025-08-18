import streamlit as st
import subprocess
import platform
import os
import google.generativeai as genai
from langchain.agents import tool
from dotenv import load_dotenv


st.set_page_config(page_title="AI Tools", layout="centered")


st.markdown("""
<style>
    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom right, #23074d, #cc5333);
        color: white;
        animation: fadeSlideIn 1.2s ease-in-out;
    }

    section[data-testid="stSidebar"] .css-1d391kg {
        color: #ffdd57 !important;
        font-size: 20px;
        font-weight: bold;
        padding-bottom: 10px;
    }

    section[data-testid="stSidebar"] a {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 0.6rem 1rem;
        margin: 5px 0;
        color: #fff !important;
        font-weight: 500;
        border: 1px solid #aaa;
        transition: all 0.3s ease-in-out;
        display: block;
        text-align: center;
    }

    section[data-testid="stSidebar"] a:hover {
        background-color: #fcd303;
        color: #1b1b1b !important;
        transform: scale(1.05);
        border-color: #fcd303;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }

    @keyframes fadeSlideIn {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
</style>
""", unsafe_allow_html=True)


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@tool
def get_date(_: str = "") -> str:
    """Returns the current system date."""
    try:
        command = "date /T" if platform.system() == "Windows" else "date"
        output = subprocess.check_output(command, shell=True)
        return output.decode().strip()
    except Exception as e:
        return f"Failed to get date: {e}"

@tool
def get_calendar(_: str = "") -> str:
    """Returns the current calendar (Linux only)."""
    if platform.system() != "Linux":
        return "The 'cal' command is only available on Linux."
    try:
        output = subprocess.check_output("cal", shell=True)
        return output.decode().strip()
    except Exception as e:
        return f"Failed to get calendar: {e}"

@tool
def get_ip_config(_: str = "") -> str:
    """Shows network configuration."""
    try:
        if platform.system() == "Windows":
            command = "ipconfig"
        else:
            try:
                command = "ifconfig"
                output = subprocess.check_output(command, shell=True)
            except:
                command = "ip a"
                output = subprocess.check_output(command, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"Failed to get IP config: {e}"

@tool
def list_files(_: str = "") -> str:
    """Lists files in the current directory."""
    try:
        command = "dir" if platform.system() == "Windows" else "ls -l"
        output = subprocess.check_output(command, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"Failed to list files: {e}"

@tool
def make_directory(dir_name: str) -> str:
    """Creates a directory with the given name."""
    try:
        os.makedirs(dir_name, exist_ok=True)
        return f"Directory '{dir_name}' created successfully."
    except Exception as e:
        return f"Failed to create directory: {e}"


def get_tool_from_query(query: str):
    tool_map = {
        "date": get_date,
        "calendar": get_calendar,
        "cal": get_calendar,
        "ip": get_ip_config,
        "network": get_ip_config,
        "list": list_files,
        "ls": list_files,
        "dir": list_files,
        "make": make_directory,
        "mkdir": make_directory
    }
    for key, func in tool_map.items():
        if key in query.lower():
            return func
    return None

def extract_directory_name(query: str) -> str:
    tokens = query.strip().split()
    for i, word in enumerate(tokens):
        if word.lower() in ["named", "name", "called", "folder"]:
            if i + 1 < len(tokens):
                return tokens[i + 1]
    return "new_folder"


st.title("🛠️ AI Tools Assistant")
st.caption("🧑‍💻 Run basic Linux & Windows commands using AI-powered tools")

with st.expander("📜 Available Commands", expanded=True):
    st.markdown("""
- **📆 System Date**: `run date`, `get date`
- **📅 Calendar** _(Linux only)_: `get calendar`, `show cal`
- **🌐 IP Configuration**: `show ip config`, `network status`, `get ip`
- **📁 List Files**: `list files`, `dir`, `ls`
- **📂 Make Directory**: `make folder named test`, `create directory called logs`
""")


user_input = st.text_input("🔎 Enter your command:", placeholder="e.g., run date, list files, create folder named test")

if user_input:
    with st.spinner("⚙️ Running..."):
        tool_fn = get_tool_from_query(user_input)
        if not tool_fn:
            st.error("🚫 No matching tool found.")
        else:
            if tool_fn == make_directory:
                folder_name = extract_directory_name(user_input)
                result = tool_fn.run(folder_name)
            else:
                result = tool_fn.run("")
            st.code(result, language="bash")


import streamlit_extras.switch_page_button as spb

# --- 🎯 NEXT PAGE BUTTON ---
# List all your page titles in correct sidebar order
page_sequence = [
    "Homepage",
    "Registration",
    "Payment",
    "Ticket_Check",
    "My_AI_Bot",
    "Web_Scrapping",
    "Prompt",
    "AI_Agents",
    "AI_Disease_Assistant",
    "Python_Task",
    "Menu_CLI",
    "JavaScript_Task",
    "Machine_Learning_project",
    "Titanic",
    "Salary_Prediction",
    "Project_Links",
    "Task_Link",
]



current_title = "AI_Agents"


if current_title in page_sequence:
    current_index = page_sequence.index(current_title)
    if current_index < len(page_sequence) - 1:
        next_page = page_sequence[current_index + 1]
        st.markdown(
            f"""
            <div style='position: fixed; bottom: 30px; right: 30px;'>
                <form action='/{next_page}'>
                    <button style='
                        background-color: #ffcc00;
                        color: #000;
                        border: none;
                        padding: 10px 20px;
                        font-size: 16px;
                        border-radius: 8px;
                        cursor: pointer;
                        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);'>
                        Next →
                    </button>
                </form>
            </div>
            """,
            unsafe_allow_html=True
        )
