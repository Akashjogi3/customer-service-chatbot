
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random
import re

# -------------------- COLORS --------------------

COLORS = {
    "background": "#F3F6FB",
    "sidebar": "#172554",
    "sidebar_hover": "#243B75",
    "primary": "#4F46E5",
    "primary_hover": "#4338CA",
    "white": "#FFFFFF",
    "text": "#1F2937",
    "muted": "#6B7280",
    "border": "#E5E7EB",
    "bot_bubble": "#FFFFFF",
    "user_bubble": "#E0E7FF",
    "success": "#16A34A",
    "input_bg": "#FFFFFF",
}

# -------------------- FAQ DATA --------------------

FAQS = [
    {
        "title": "Order Tracking",
        "keywords": ["track order", "tracking", "where is my order",
                     "order status", "delivery status", "package"],
        "question": "Where is my order?",
        "answer": (
            "You can check your order status from the Orders section "
            "of your account. Use your order ID to find the latest "
            "tracking information."
        ),
    },
    {
        "title": "Returns and Refunds",
        "keywords": ["refund", "return", "money back", "exchange",
                     "cancel order", "cancellation"],
        "question": "How can I request a refund?",
        "answer": (
            "To request a refund, open your Orders section and select "
            "the item you want to return. Follow the return instructions. "
            "Refund processing times depend on the payment method and "
            "the company's return policy."
        ),
    },
    {
        "title": "Payment Problems",
        "keywords": ["payment", "paid", "transaction", "debit",
                     "credit card", "upi", "payment failed"],
        "question": "What if my payment fails?",
        "answer": (
            "First, check whether the amount was deducted from your "
            "account. If it was deducted, avoid making the same payment "
            "again immediately. Check your order history and contact "
            "customer support if the issue continues."
        ),
    },
    {
        "title": "Account Help",
        "keywords": ["account", "login", "log in", "password",
                     "sign in", "forgot password", "register"],
        "question": "I cannot log in to my account.",
        "answer": (
            "Check that your email address and password are correct. "
            "If you forgot your password, use the Forgot Password "
            "option on the login page to reset it."
        ),
    },
    {
        "title": "Shipping Information",
        "keywords": ["shipping", "delivery", "deliver", "shipping fee",
                     "delivery time", "address"],
        "question": "How long does delivery take?",
        "answer": (
            "Delivery time depends on your location and the shipping "
            "method. Check the estimated delivery date in your order "
            "details for more information."
        ),
    },
    {
        "title": "Contact Support",
        "keywords": ["contact", "human", "agent", "representative",
                     "support team", "customer care", "phone number"],
        "question": "How can I contact customer support?",
        "answer": (
            "You can contact the customer support team through the "
            "Help or Contact Us section of the company's website. "
            "Keep your order number ready if your question is about "
            "a specific order."
        ),
    },
    {
        "title": "Working Hours",
        "keywords": ["working hours", "business hours", "open",
                     "opening time", "available", "hours"],
        "question": "What are your support hours?",
        "answer": (
            "This demo chatbot is available whenever you run it. "
            "Actual customer service hours depend on the company."
        ),
    },
]

GREETINGS = [
    "Hello! Welcome to Customer Support. How can I help you today?",
    "Hi there! I'm your virtual support assistant. What can I help you with?",
    "Hello! Feel free to ask me about orders, payments, refunds, or accounts.",
]

THANK_YOU_RESPONSES = [
    "You're welcome! I'm happy to help.",
    "You're welcome! Let me know if you have another question.",
    "Glad I could help. Have a great day!",
]

# -------------------- RESPONSE LOGIC --------------------

def normalize(text):
    """Convert text into a consistent searchable format."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text)


def contains_phrase(text, phrase):
    """Match a complete phrase instead of an accidental substring."""
    text = f" {normalize(text)} "
    phrase = f" {normalize(phrase)} "
    return phrase in text


def get_response(user_text):
    """Choose an appropriate response based on the user's message."""
    text = normalize(user_text)

    if not text:
        return "Please type a question so I can help you."

    greeting_words = ["hello", "hi", "hey", "good morning",
                      "good afternoon", "good evening"]

    if any(contains_phrase(text, word) for word in greeting_words):
        return random.choice(GREETINGS)

    if any(contains_phrase(text, word) for word in
           ["thank you", "thanks", "thank u", "thx"]):
        return random.choice(THANK_YOU_RESPONSES)

    if any(contains_phrase(text, word) for word in
           ["bye", "goodbye", "see you"]):
        return "Goodbye! Thank you for chatting with Customer Support."

    if "help" in text and len(text.split()) <= 3:
        return (
            "Of course! I can help with order tracking, refunds, "
            "payments, account problems, shipping, and customer support. "
            "What would you like to know?"
        )

    # Search the FAQ topics.
    for faq in FAQS:
        if any(contains_phrase(text, keyword)
               for keyword in faq["keywords"]):
            return faq["answer"]

    if any(word in text for word in ["price", "cost", "discount", "offer"]):
        return (
            "For prices, discounts, and current offers, please check "
            "the product page on the company's website."
        )

    if any(word in text for word in ["complaint", "problem", "issue", "wrong"]):
        return (
            "I'm sorry you're experiencing a problem. Please describe "
            "the issue in more detail, or contact the customer support "
            "team for assistance with your specific case."
        )

    return (
        "I'm sorry, I couldn't find an exact answer to that question. "
        "Try asking about order tracking, refunds, payments, account "
        "problems, shipping, or contacting support."
    )


# -------------------- CHAT FUNCTIONS --------------------

def add_message(sender, message):
    """Display a chat message with its time."""
    is_user = sender == "You"

    outer = tk.Frame(chat_area, bg=COLORS["background"])
    outer.pack(fill="x", padx=16, pady=6)

    alignment = "e" if is_user else "w"
    bubble_color = (
        COLORS["user_bubble"] if is_user else COLORS["bot_bubble"]
    )

    content = tk.Frame(outer, bg=COLORS["background"])
    content.pack(anchor=alignment)

    name = tk.Label(
        content,
        text=sender,
        font=("Segoe UI", 9, "bold"),
        bg=COLORS["background"],
        fg=COLORS["muted"],
    )
    name.pack(anchor=alignment, padx=4)

    bubble = tk.Label(
        content,
        text=message,
        font=("Segoe UI", 10),
        bg=bubble_color,
        fg=COLORS["text"],
        wraplength=430,
        justify="left",
        padx=14,
        pady=10,
        relief="flat",
        bd=0,
    )
    bubble.pack(anchor=alignment, pady=(3, 2))

    timestamp = datetime.now().strftime("%I:%M %p")
    time_label = tk.Label(
        content,
        text=timestamp,
        font=("Segoe UI", 8),
        bg=COLORS["background"],
        fg=COLORS["muted"],
    )
    time_label.pack(anchor=alignment, padx=4)

    # Automatically scroll to the latest message.
    chat_area.update_idletasks()
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))
    chat_canvas.yview_moveto(1.0)


def send_message(event=None):
    """Send the user's message and display the chatbot response."""
    if is_busy[0]:
        return "break"

    message = message_entry.get().strip()

    if message == "" or message == PLACEHOLDER:
        return "break"

    add_message("You", message)

    message_entry.delete(0, tk.END)
    message_entry.config(fg=COLORS["text"])

    is_busy[0] = True
    send_button.config(state="disabled", text="Sending...")
    status_label.config(text="● Assistant is typing...", fg="#F59E0B")

    typing_label = tk.Label(
        chat_area,
        text="Assistant is typing...",
        font=("Segoe UI", 9, "italic"),
        bg=COLORS["background"],
        fg=COLORS["muted"],
    )
    typing_label.pack(anchor="w", padx=22, pady=5)

    chat_area.update_idletasks()
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))
    chat_canvas.yview_moveto(1.0)

    # Simulate a short typing delay.
    root.after(
        650,
        lambda: finish_response(message, typing_label)
    )

    return "break"


def finish_response(user_message, typing_label):
    """Display the chatbot response after the typing animation."""
    try:
        typing_label.destroy()
    except tk.TclError:
        pass

    response = get_response(user_message)
    add_message("Assistant", response)

    is_busy[0] = False
    send_button.config(state="normal", text="Send")
    status_label.config(text="● Online", fg=COLORS["success"])
    message_entry.focus_set()


def ask_question(question):
    """Send a suggested question through the regular chat flow."""
    if is_busy[0]:
        return

    remove_placeholder()
    message_entry.delete(0, tk.END)
    message_entry.insert(0, question)
    message_entry.config(fg=COLORS["text"])
    send_message()


def clear_chat():
    """Clear all messages after user confirmation."""
    if messagebox.askyesno(
        "Clear Chat",
        "Are you sure you want to clear this conversation?",
        parent=root,
    ):
        for widget in chat_area.winfo_children():
            widget.destroy()

        show_welcome_message()


def show_welcome_message():
    add_message(
        "Assistant",
        "Welcome to Customer Support!\n\n"
        "I'm here to help you with your questions. You can ask about "
        "orders, refunds, payments, shipping, or your account.\n\n"
        "You can also choose a topic from the left sidebar."
    )


# -------------------- SIDEBAR FUNCTIONS --------------------

def filter_topics(*args):
    """Filter FAQ topic buttons using the search box."""
    query = normalize(search_var.get())

    for widget in topic_list.winfo_children():
        widget.destroy()

    matches = []

    for faq in FAQS:
        searchable = normalize(
            faq["title"] + " " + " ".join(faq["keywords"])
        )

        if query in searchable:
            matches.append(faq)

    if not matches:
        tk.Label(
            topic_list,
            text="No topics found",
            bg=COLORS["sidebar"],
            fg="#CBD5E1",
            font=("Segoe UI", 10),
        ).pack(anchor="w", padx=12, pady=10)
        return

    for faq in matches:
        button = tk.Button(
            topic_list,
            text="  " + faq["title"],
            command=lambda item=faq: ask_question(item["question"]),
            anchor="w",
            font=("Segoe UI", 10),
            bg=COLORS["sidebar"],
            fg="white",
            activebackground=COLORS["sidebar_hover"],
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=10,
            cursor="hand2",
        )
        button.pack(fill="x", pady=2)

        button.bind(
            "<Enter>",
            lambda event, b=button:
                b.config(bg=COLORS["sidebar_hover"])
        )
        button.bind(
            "<Leave>",
            lambda event, b=button:
                b.config(bg=COLORS["sidebar"])
        )


def close_app():
    if messagebox.askyesno(
        "Exit Chatbot",
        "Do you want to close the chatbot?",
        parent=root,
    ):
        root.destroy()


# -------------------- MAIN WINDOW --------------------

root = tk.Tk()
root.title("Customer Support Chatbot")
root.geometry("1050x720")
root.minsize(850, 600)
root.configure(bg=COLORS["background"])

is_busy = [False]

# -------------------- SIDEBAR --------------------

sidebar = tk.Frame(root, bg=COLORS["sidebar"], width=255)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

brand = tk.Frame(sidebar, bg=COLORS["sidebar"])
brand.pack(fill="x", padx=20, pady=(25, 20))

tk.Label(
    brand,
    text="CS",
    font=("Segoe UI", 19, "bold"),
    bg=COLORS["primary"],
    fg="white",
    width=3,
    height=1,
).pack(anchor="w", pady=(0, 10))

tk.Label(
    brand,
    text="Customer Support",
    font=("Segoe UI", 16, "bold"),
    bg=COLORS["sidebar"],
    fg="white",
).pack(anchor="w")

tk.Label(
    brand,
    text="VIRTUAL ASSISTANT",
    font=("Segoe UI", 9, "bold"),
    bg=COLORS["sidebar"],
    fg="#93C5FD",
).pack(anchor="w", pady=(4, 0))

tk.Label(
    sidebar,
    text="HELP TOPICS",
    font=("Segoe UI", 9, "bold"),
    bg=COLORS["sidebar"],
    fg="#94A3B8",
).pack(anchor="w", padx=20, pady=(12, 8))

search_var = tk.StringVar()

search_entry = tk.Entry(
    sidebar,
    textvariable=search_var,
    font=("Segoe UI", 10),
    bg="#243B75",
    fg="white",
    insertbackground="white",
    relief="flat",
    bd=0,
)
search_entry.pack(fill="x", padx=16, pady=(0, 12), ipady=9)

search_entry.insert(0, "Search topics...")
search_entry.config(fg="#CBD5E1")


def search_focus_in(event):
    if search_entry.get() == "Search topics...":
        search_entry.delete(0, tk.END)
        search_entry.config(fg="white")


def search_focus_out(event):
    if not search_entry.get().strip():
        search_entry.insert(0, "Search topics...")
        search_entry.config(fg="#CBD5E1")


def handle_search(*args):
    if search_entry.get() == "Search topics...":
        search_var.set("")
    filter_topics()


search_entry.bind("<FocusIn>", search_focus_in)
search_entry.bind("<FocusOut>", search_focus_out)
search_var.trace_add("write", handle_search)

topic_list = tk.Frame(sidebar, bg=COLORS["sidebar"])
topic_list.pack(fill="both", expand=True, padx=8, pady=(0, 12))

filter_topics()

sidebar_bottom = tk.Frame(sidebar, bg=COLORS["sidebar"])
sidebar_bottom.pack(fill="x", side="bottom", padx=16, pady=18)

tk.Label(
    sidebar_bottom,
    text="Demo Project | Python + Tkinter",
    font=("Segoe UI", 8),
    bg=COLORS["sidebar"],
    fg="#94A3B8",
).pack(anchor="w", pady=(0, 10))

tk.Button(
    sidebar_bottom,
    text="Clear Conversation",
    command=clear_chat,
    font=("Segoe UI", 10),
    bg="#243B75",
    fg="white",
    activebackground="#334D8C",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    pady=9,
).pack(fill="x")

# -------------------- CHAT MAIN PANEL --------------------

main_panel = tk.Frame(root, bg=COLORS["background"])
main_panel.pack(side="left", fill="both", expand=True)

# Header
header = tk.Frame(
    main_panel,
    bg=COLORS["white"],
    highlightbackground=COLORS["border"],
    highlightthickness=1,
)
header.pack(fill="x")

header_left = tk.Frame(header, bg=COLORS["white"])
header_left.pack(side="left", padx=24, pady=16)

tk.Label(
    header_left,
    text="Customer Service Chatbot",
    font=("Segoe UI", 16, "bold"),
    bg=COLORS["white"],
    fg=COLORS["text"],
).pack(anchor="w")

tk.Label(
    header_left,
    text="Ask questions and get instant assistance",
    font=("Segoe UI", 9),
    bg=COLORS["white"],
    fg=COLORS["muted"],
).pack(anchor="w", pady=(3, 0))

status_label = tk.Label(
    header,
    text="● Online",
    font=("Segoe UI", 10, "bold"),
    bg=COLORS["white"],
    fg=COLORS["success"],
)
status_label.pack(side="right", padx=24)

# Chat message area with scrolling
chat_container = tk.Frame(main_panel, bg=COLORS["background"])
chat_container.pack(fill="both", expand=True)

chat_canvas = tk.Canvas(
    chat_container,
    bg=COLORS["background"],
    highlightthickness=0,
)

chat_scrollbar = tk.Scrollbar(
    chat_container,
    orient="vertical",
    command=chat_canvas.yview,
)

chat_area = tk.Frame(chat_canvas, bg=COLORS["background"])

chat_area_window = chat_canvas.create_window(
    (0, 0),
    window=chat_area,
    anchor="nw",
)

chat_area.bind(
    "<Configure>",
    lambda event: chat_canvas.configure(
        scrollregion=chat_canvas.bbox("all")
    ),
)

chat_canvas.bind(
    "<Configure>",
    lambda event: chat_canvas.itemconfigure(
        chat_area_window,
        width=event.width,
    ),
)

chat_canvas.configure(yscrollcommand=chat_scrollbar.set)

chat_canvas.pack(side="left", fill="both", expand=True)
chat_scrollbar.pack(side="right", fill="y")


def on_mousewheel(event):
    chat_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


chat_canvas.bind_all("<MouseWheel>", on_mousewheel)

# -------------------- SUGGESTED QUESTIONS --------------------

suggestion_panel = tk.Frame(
    main_panel,
    bg=COLORS["background"],
)
suggestion_panel.pack(fill="x", padx=18, pady=(5, 8))

tk.Label(
    suggestion_panel,
    text="QUICK QUESTIONS",
    font=("Segoe UI", 8, "bold"),
    bg=COLORS["background"],
    fg=COLORS["muted"],
).pack(anchor="w", pady=(0, 7))

suggestions = tk.Frame(suggestion_panel, bg=COLORS["background"])
suggestions.pack(fill="x")

suggestion_questions = [
    "Track my order",
    "Request a refund",
    "Payment failed",
    "Login problem",
]

for question in suggestion_questions:
    tk.Button(
        suggestions,
        text=question,
        command=lambda q=question: ask_question(q),
        font=("Segoe UI", 9),
        bg=COLORS["white"],
        fg=COLORS["primary"],
        activebackground="#EEF2FF",
        activeforeground=COLORS["primary_hover"],
        relief="flat",
        highlightbackground=COLORS["border"],
        highlightthickness=1,
        cursor="hand2",
        padx=10,
        pady=7,
    ).pack(side="left", padx=(0, 7), pady=2)

# -------------------- MESSAGE INPUT --------------------

input_panel = tk.Frame(
    main_panel,
    bg=COLORS["white"],
    highlightbackground=COLORS["border"],
    highlightthickness=1,
)
input_panel.pack(fill="x", padx=18, pady=(0, 15))

input_inner = tk.Frame(input_panel, bg=COLORS["white"])
input_inner.pack(fill="x", padx=12, pady=12)

tk.Label(
    input_inner,
    text="Message",
    font=("Segoe UI", 9, "bold"),
    bg=COLORS["white"],
    fg=COLORS["text"],
).pack(anchor="w", pady=(0, 7))

input_row = tk.Frame(input_inner, bg=COLORS["white"])
input_row.pack(fill="x")

PLACEHOLDER = "Type your question here..."


def remove_placeholder(event=None):
    if message_entry.get() == PLACEHOLDER:
        message_entry.delete(0, tk.END)
        message_entry.config(fg=COLORS["text"])


def add_placeholder(event=None):
    if not message_entry.get().strip():
        message_entry.delete(0, tk.END)
        message_entry.insert(0, PLACEHOLDER)
        message_entry.config(fg=COLORS["muted"])


message_entry = tk.Entry(
    input_row,
    font=("Segoe UI", 11),
    bg=COLORS["input_bg"],
    fg=COLORS["muted"],
    insertbackground=COLORS["text"],
    relief="solid",
    bd=1,
)
message_entry.pack(side="left", fill="x", expand=True, ipady=12, padx=(0, 10))

message_entry.insert(0, PLACEHOLDER)
message_entry.bind("<FocusIn>", remove_placeholder)
message_entry.bind("<FocusOut>", add_placeholder)
message_entry.bind("<Return>", send_message)

send_button = tk.Button(
    input_row,
    text="Send",
    command=send_message,
    font=("Segoe UI", 10, "bold"),
    bg=COLORS["primary"],
    fg="white",
    activebackground=COLORS["primary_hover"],
    activeforeground="white",
    disabledforeground="#E5E7EB",
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=24,
    pady=11,
)
send_button.pack(side="right")

send_button.bind(
    "<Enter>",
    lambda event: (
        send_button.config(bg=COLORS["primary_hover"])
        if str(send_button["state"]) == "normal"
        else None
    ),
)

send_button.bind(
    "<Leave>",
    lambda event: (
        send_button.config(bg=COLORS["primary"])
        if str(send_button["state"]) == "normal"
        else None
    ),
)

tk.Label(
    input_inner,
    text="Press Enter to send your message.",
    font=("Segoe UI", 8),
    bg=COLORS["white"],
    fg=COLORS["muted"],
).pack(anchor="w", pady=(7, 0))

# -------------------- START CHATBOT --------------------

show_welcome_message()
message_entry.focus_set()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
