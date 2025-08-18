import streamlit as st
import paramiko
import streamlit.components.v1 as components


st.set_page_config(
    page_title="🛠️ All-in-One SSH + Web App",
    page_icon="🌐",
    layout="wide"
)


st.markdown("""
<style>
    /* Sidebar styling (unchanged) */
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

st.title("🛠️ Multi-Feature SSH Linux & Docker")

st.sidebar.title("📚 Menu")
menu = st.sidebar.radio(
    "Choose Module",
    ["Linux", "Docker"]
)


if menu != "Web App":
    st.header("🔑 SSH Connection Details")
    hostname = st.text_input("Server IP", placeholder="e.g. 192.168.1.10")
    username = st.text_input("Username", value="root")
    password = st.text_input("Password", type="password")

    if "ssh_client" not in st.session_state:
        st.session_state.ssh_client = None

    if st.button("Connect"):
        if not hostname or not username or not password:
            st.warning("⚠️ Please fill in all SSH details.")
        else:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(hostname, username=username, password=password, timeout=10)
                st.session_state.ssh_client = ssh
                st.success(f"✅ Connected to {hostname} as {username}")
            except Exception as e:
                st.error(f"❌ SSH connection failed: {e}")
                st.session_state.ssh_client = None



if menu == "Linux":
    st.header("🐧 Linux Command Manager")

    commands = [
        "whoami", "hostname", "uname -a", "date", "uptime", "pwd", "ls -l", "ls -la",
        "mkdir test_dir", "rm -rf test_dir", "cp file1 file2", "mv file1 file2",
        "touch newfile.txt", "cat filename", "tail -n 10 filename", "head -n 10 filename",
        "df -h", "free -m", "ps aux", "top -n 1 -b", "systemctl status", "journalctl -xe",
        "ifconfig", "ip addr", "ping google.com", "traceroute google.com", "netstat -tuln",
        "ss -tuln", "echo Hello World", "reboot ⚠️", "shutdown now ⚠️", "Custom Command"
    ]

    selected = st.selectbox("Select Linux command", commands)

    if selected == "Custom Command":
        command = st.text_area("📝 Enter your command", "echo Hello World")
    elif selected in ["cat filename", "tail -n 10 filename", "head -n 10 filename"]:
        file = st.text_input("📂 Filename")
        if selected.startswith("cat"):
            command = f"cat {file}"
        elif selected.startswith("tail"):
            command = f"tail -n 10 {file}"
        else:
            command = f"head -n 10 {file}"
    elif selected == "cp file1 file2":
        src = st.text_input("Source file")
        dst = st.text_input("Destination file")
        command = f"cp {src} {dst}"
    elif selected == "mv file1 file2":
        src = st.text_input("Source file")
        dst = st.text_input("Destination file")
        command = f"mv {src} {dst}"
    else:
        command = selected

    if st.button("🚀 Run Linux Command"):
        if st.session_state.ssh_client:
            ssh = st.session_state.ssh_client
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()

            st.subheader("📄 Output")
            st.code(output if output else "(No output)")

            if error:
                st.subheader("⚠️ Error")
                st.code(error)
        else:
            st.warning("⚠️ Please connect first!")

elif menu == "Docker":
    st.header("🐳 Docker Command Manager")

    if st.session_state.ssh_client:
        options = [
            "docker --version", "docker version", "docker info", "docker login", "docker logout",
            "docker images", "docker pull", "docker rmi", "docker ps", "docker ps -a",
            "docker start", "docker stop", "docker restart", "docker rm", "docker exec",
            "docker logs", "docker inspect", "docker build", "docker run",
            "docker container prune -f", "docker image prune -f", "docker network ls",
            "docker network inspect", "docker network prune -f", "docker volume ls",
            "docker volume inspect", "docker volume prune -f", "date", "Custom command"
        ]

        selected = st.selectbox("Pick Docker command", options)

        if selected == "Custom command":
            command = st.text_input("Enter your custom Docker command:")
        elif selected in ["docker stop", "docker start", "docker restart", "docker rm", "docker logs", "docker inspect"]:
            container_id = st.text_input("Container ID:")
            command = f"{selected} {container_id}"
        elif selected == "docker exec":
            container_id = st.text_input("Container ID:")
            exec_cmd = st.text_input("Command inside container:")
            command = f"docker exec {container_id} {exec_cmd}"
        elif selected == "docker pull":
            image_name = st.text_input("Image name:")
            tag = st.text_input("Tag:", value="latest")
            command = f"docker pull {image_name}:{tag}"
        elif selected == "docker rmi":
            image_name = st.text_input("Image name:")
            tag = st.text_input("Tag (optional):")
            command = f"docker rmi {image_name}:{tag}" if tag else f"docker rmi {image_name}"
        elif selected == "docker build":
            image_name = st.text_input("Image name:")
            tag = st.text_input("Tag:")
            path = st.text_input("Path to Dockerfile:")
            command = f"docker build -t {image_name}:{tag} {path}"
        elif selected == "docker run":
            image_name = st.text_input("Image name (with tag):")
            options_run = st.text_input("Options (e.g. -it --rm):", value="-it --rm")
            cmd_inside = st.text_input("Command inside container:", value="/bin/bash")
            command = f"docker run {options_run} {image_name} {cmd_inside}"
        else:
            command = selected

        if st.button("🐳 Run Docker Command"):
            ssh = st.session_state.ssh_client
            stdin, stdout, stderr = ssh.exec_command(command)
            out = stdout.read().decode()
            err = stderr.read().decode()

            st.subheader("✅ Output")
            st.code(out if out else "(No output)")

            if err:
                st.subheader("⚠️ Errors")
                st.code(err)
    else:
        st.warning("⚠️ Please connect first!")



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

current_title = "Menu_CLI"

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
