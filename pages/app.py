import flet as ft
import json

def main(page: ft.Page):
    page.title = "Login Screen"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def open_chat(profile):
        page.snack_bar = ft.SnackBar(
            ft.Text(f"Opening chat with {profile['name']}"),
            bgcolor=ft.colors.GREEN,
        )
        page.snack_bar.open = True
        page.update()

    def main_page_content():
        page.clean()
        page.title = "ConvoHub"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.padding = 20

        messages = [
            {"name": "Ddedida", "message": "Ayo sholat Jumat", "time": "11.43", "new_messages": 1},
            {"name": "Remaja Masjid", "message": "Kapan sholat rek", "time": "10.55", "new_messages": 1},
            {"name": "Intger", "message": "Ayo sholat Isya", "time": "Yesterday", "new_messages": 1}
        ]

        message_list = []
        for msg in messages:
            message_list.append(
                ft.ListTile(
                    leading=ft.CircleAvatar(
                        content=ft.Text(
                            msg["name"][0],
                            style=ft.TextStyle(color=ft.colors.WHITE, size=20)
                        ),
                        bgcolor=ft.colors.PURPLE,
                        radius=20
                    ),
                    title=ft.Text(msg["name"], weight=ft.FontWeight.BOLD),
                    height=70,
                    on_click=lambda e, msg=msg: open_chat(msg)  # Make each profile clickable
                )
            )

        create_group_button = ft.ElevatedButton(
            text="Create New Group",
            icon=ft.icons.GROUP_ADD,
            on_click=lambda e: print("Create New Group Clicked")
        )

        chat_room_messages = []

        def send_message(e):
            message = message_input.value
            if message:
                chat_room_messages.append(ft.Text(message))
                message_input.value = ""
                page.update()

        message_input = ft.TextField(hint_text="Type a message", expand=True, border_color=ft.colors.WHITE)
        send_button = ft.ElevatedButton(text="Send", on_click=send_message)

        chat_room = ft.Container(
            content=ft.Column([
                ft.Text("Chat Room", style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD)),
                ft.Column(chat_room_messages, expand=True),
                ft.Row(
                    [
                        message_input,
                        send_button
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    spacing=10
                )
            ]),
            expand=True
        )

        page.add(
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Row([ft.Text("ConvoHub.", style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD))]),
                            ft.Row([create_group_button]),
                            ft.Column(message_list, spacing=10, width=350),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.START
                    ),
                    ft.Container(
                        width=1,
                        bgcolor=ft.colors.GREY,
                        # expand=True
                    ),
                    chat_room
                ],
                expand=True
            )
        )

    def login_page_content():
        page.clean()
        page.title = "Login Screen"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        def on_login(e):
            username = username_field.value
            password = password_field.value

            # Read the JSON file with user data
            try:
                with open('../db/user.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                print("User database not found.")
                page.snack_bar = ft.SnackBar(
                    ft.Text("User database not found.", color=ft.colors.WHITE),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                page.update()
                return

            # Check the provided credentials
            if username in data and data[username] == password:
                print("Login Successful")
                main_page_content()  # Switch to main page content
            else:
                print("Username or Password Incorrect")
                page.snack_bar = ft.SnackBar(
                    ft.Text("Username or Password Incorrect", color=ft.colors.WHITE),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                page.update()

        username_field = ft.TextField(label="username", hint_text="username.example.com", width=300)
        password_field = ft.TextField(label="Password", password=True, width=300)

        login_button = ft.ElevatedButton(
            text="Log in",
            on_click=on_login,
            width=300,
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
        )

        signup_text = ft.TextButton(
            text="Sign Up",
            on_click=lambda e: print("Navigate to Sign Up"),
        )

        forgot_password_text = ft.TextButton(
            text="Forgot Password?",
            on_click=lambda e: print("Navigate to Forgot Password"),
        )

        page.add(
            ft.Column(
                [
                    ft.Text("Let's sign you in!", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Welcome back, you have been missed :(", size=16),
                    username_field,
                    password_field,
                    forgot_password_text,
                    login_button,
                    ft.Row(
                        [
                            ft.Text("Don't have an account? "),
                            signup_text,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )

    login_page_content()

ft.app(target=main)