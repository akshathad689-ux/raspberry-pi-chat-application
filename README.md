# Raspberry Pi WebSocket Chat 💬🍓

A browser-based real-time chat application developed using **Raspberry Pi, Python, WebSocket, and HTML**.

This project allows multiple users connected to the same **Local Area Network (LAN)** to communicate with each other in real time through a web browser.

The **Raspberry Pi acts as the central server**, managing WebSocket connections and broadcasting messages between connected clients.

---

## 📌 Project Overview

The **Raspberry Pi WebSocket Chat** is a real-time browser-based communication system designed to demonstrate the use of **WebSocket technology with Raspberry Pi**.

WebSocket provides a persistent connection between the client and server, allowing messages to be exchanged instantly without repeatedly requesting data from the server.

Multiple users can connect to the Raspberry Pi server using their web browsers and communicate through the same chat application.

This project combines **IoT, networking, Python programming, WebSocket communication, and web development** into a practical application.

---

## 🎯 Objectives

The main objectives of this project are:

- To understand WebSocket-based communication
- To learn client-server architecture
- To use Raspberry Pi as a local network server
- To develop a browser-based chat application
- To implement real-time communication
- To handle multiple connected clients
- To understand message broadcasting
- To gain practical experience with Python networking
- To understand communication over a Local Area Network

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Raspberry Pi 4 Model B** | Acts as the central server |
| **Python 3** | Backend programming |
| **WebSocket** | Real-time communication |
| **HTML** | Web-based chat interface |
| **JavaScript** | Client-side communication |
| **Wi-Fi / LAN** | Network connectivity |
| **Web Browser** | Client interface |

---

## 🏗️ System Architecture

```text
                         ┌───────────────────────┐
                         │      Raspberry Pi     │
                         │                       │
                         │   Python WebSocket    │
                         │       Server          │
                         └───────────┬───────────┘
                                     │
                                  Wi-Fi / LAN
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
              ▼                      ▼                      ▼
       ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
       │   Browser   │       │   Browser   │       │   Browser   │
       │   Client 1  │       │   Client 2  │       │   Client 3  │
       └─────────────┘       └─────────────┘       └─────────────┘
