import tkinter as tk
from tkinter import ttk, messagebox
from port_scanner import scan_ports
from web_crawler import crawl_website
from file_transfer import send_file
from tkinter import filedialog
from wiki_fetcher import fetch_wikipedia_summary
from network_scanner import scan_network

def show_port_scanner():
    def run_scan():
        host = entry_host.get()
        try:
            start_port = int(entry_start_port.get())
            end_port = int(entry_end_port.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Ports must be integers.")
            return

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Scanning {host} from port {start_port} to {end_port}...\n\n")

        open_ports = scan_ports(host, start_port, end_port)

        if open_ports:
            for port, service in open_ports:
                result_text.insert(tk.END, f"Port {port} open ({service})\n")
        else:
            result_text.insert(tk.END, "No open ports found.")

    # Clear window
    for widget in window.winfo_children():
        widget.destroy()

    # Create the main frame
    frame = tk.Frame(window)
    frame.pack(pady=20)

    # Heading
    tk.Label(frame, text="Port Scanner", font=("Arial", 16)).pack(pady=10)

    # Form frame for inputs
    form_frame = tk.Frame(frame)
    form_frame.pack()

    tk.Label(form_frame, text="Host/IP:").grid(row=0, column=0, padx=5, pady=5)
    entry_host = tk.Entry(form_frame)
    entry_host.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Start Port:").grid(row=1, column=0, padx=5, pady=5)
    entry_start_port = tk.Entry(form_frame)
    entry_start_port.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="End Port:").grid(row=2, column=0, padx=5, pady=5)
    entry_end_port = tk.Entry(form_frame)
    entry_end_port.grid(row=2, column=1, padx=5, pady=5)

    # Buttons
    button_frame = tk.Frame(frame)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Scan", command=run_scan).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Back to Main Menu", command=main_menu).pack(side=tk.LEFT, padx=10)

    # Results
    result_text = tk.Text(frame, height=15, width=60)
    result_text.pack(pady=10)

def show_web_crawler():
    def run_crawl():
        url = entry_url.get()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Crawling {url}...\n\n")

        links = crawl_website(url)

        for link in links:
            result_text.insert(tk.END, f"{link}\n")

    for widget in window.winfo_children():
        widget.destroy()

    frame = tk.Frame(window)
    frame.pack(pady=20)

    tk.Label(frame, text="Web Crawler", font=("Arial", 16)).pack(pady=10)

    tk.Label(frame, text="Enter URL:").pack()
    entry_url = tk.Entry(frame, width=50)
    entry_url.pack(pady= 5)

    button_frame = tk.Frame(frame)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Crawl", command=run_crawl).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Back to Main Menu", command=main_menu).pack(side=tk.LEFT, padx=10)

    result_text = tk.Text(frame, height=15, width=60)
    result_text.pack(pady = 10)

def show_file_transfer():
    def browse_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            entry_file.delete(0, tk.END)
            entry_file.insert(0, file_path)

    def run_transfer():
        file_path = entry_file.get()
        ip = entry_ip.get()

        if not file_path or not ip:
            messagebox.showerror("Missing Input", "Please select a file and enter server IP address.")

        result = send_file(file_path, ip)
        result_label.config(text=result)

    for widget in window.winfo_children():
        widget.destroy()

    frame = tk.Frame(window)
    frame.pack(pady=20)

    tk.Label(frame, text="File Transfer", font=("Arial", 16)).pack(pady=10)

    tk.Label(frame, text="Server IP:").pack()
    entry_ip = tk.Entry(frame, width=40)
    entry_ip.pack()

    tk.Label(frame, text="Select File:").pack()
    entry_file = tk.Entry(frame, width=50)
    entry_file.pack()
    tk.Button(frame, text="Browse", command=browse_file).pack(pady = 5)

    tk.Button(frame, text="Send File", command=run_transfer).pack(pady=10)

    result_label = tk.Label(frame, text="")
    result_label.pack()

    tk.Button(frame, text="Back to Main Menu", command=main_menu).pack(pady=10)

def show_wikipedia_fetcher():
    def run_fetch():
        topic = entry_topic.get().strip()
        if not topic:
            messagebox.showerror("Input Error", "Please enter a topic.")
            return
        summary = fetch_wikipedia_summary(topic)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, summary)

    for widget in window.winfo_children():
       widget.destroy()


    frame = tk.Frame(window)
    frame.pack(pady=20)

    tk.Label(frame, text="Wikipedia Summary Fetcher", font=("Arial", 16)).pack(pady=10)

    tk.Label(frame, text="Enter topic:").pack()
    entry_topic = tk.Entry(frame, width=40)
    entry_topic.pack(pady=5)

    tk.Button(frame, text="Fetch Summary", command=run_fetch).pack(pady=5)

    result_text = tk.Text(frame, height=15, width=60, wrap="word")
    result_text.pack(pady=10)

    tk.Button(frame, text="Back to Main Menu", command=main_menu).pack(pady=10)

def show_network_scanner():
    for widget in window.winfo_children():
        widget.destroy()

    frame = tk.Frame(window)
    frame.pack(pady=20)

    ttk.Button(frame, text="Back to Main Menu", command=main_menu).pack(pady=5)
    tk.Label(frame, text="Network Device Scanner", font=("Arial", 16)).pack(pady=10)

    tk.Label(frame, text="Enter base IP (e.g., 192.168.1.):").pack()
    base_ip_entry = tk.Entry(frame)
    base_ip_entry.pack()

    result_text = tk.Text(window, height=15, width=60)
    result_text.pack()

    def run_scan():
        base_ip = base_ip_entry.get()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Scanning network {base_ip}1 - {base_ip}254...\n\n")
        active_ips = scan_network(base_ip)
        if active_ips:
            for ip in active_ips:
                result_text.insert(tk.END, f"Active: {ip}\n")
        else:
            result_text.insert(tk.END, "No active networks found.")

    tk.Button(frame, text="Scan", command=run_scan).pack(pady=10)
def main_menu():
    for widget in window.winfo_children():
        widget.destroy()

    top_frame = tk.Frame(window)
    top_frame.pack(anchor="n", pady=10)

    tk.Label(top_frame, text="Network Toolkit", font=("Arial", 18)).pack(pady=10)

    ttk.Button(top_frame, text="1. Port Scanner", command=show_port_scanner).pack(pady=5)
    ttk.Button(top_frame, text="2. Web Crawler", command=show_web_crawler).pack(pady=5)
    ttk.Button(top_frame, text="3. File Transfer", command=show_file_transfer).pack(pady=5)
    ttk.Button(top_frame, text="4. Wikipedia Data Fetcher", command=show_wikipedia_fetcher).pack(pady=5)
    ttk.Button(top_frame, text="5. Network Device Scanner", command=show_network_scanner).pack(pady=5)

    ttk.Button(top_frame, text="Exit", command=window.quit).pack(pady=10)

# Main window
window = tk.Tk()
window.title("Network Toolkit")
window.geometry("500x600")
main_menu()
window.mainloop()
