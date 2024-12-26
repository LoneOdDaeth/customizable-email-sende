# Özelleştirilebilir E-posta Gönderici

Bu Python betiği, SMTP kullanarak gönderen ve alıcı adreslerini özelleştirebileceğiniz, ekler ekleyebileceğiniz bir e-posta gönderme çözümü sunar. E-posta gönderme görevlerini otomatikleştirmek için basit ama güçlü bir araçtır.

## Özellikler

- Gönderen ve alıcı e-posta adreslerini özelleştirme.
- Konu ve metin içeren e-postalar gönderme.
- Ek dosyaları destekler (ör. belgeler, resimler).
- Tamamen yapılandırılabilir SMTP ayarları.

## Kurulum ve Kullanım

### Gereksinimler

- Python 3.6 veya üstü
- Gerekli kütüphaneler: `smtplib`, `ssl` ve `email` (Python'da standart olarak bulunur)

### Kullanım Adımları

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/yourusername/customizable-email-sender.git
   cd customizable-email-sender
2. Betik dosyasını açın ve aşağıdaki yer tutucuları değiştirin:

- **Gönderen e-posta adresi**: "sender_mail" yerine göndermek istediğiniz e-posta adresini yazın.
- **Alıcı e-posta adresi**: "reciver_mail" yerine alıcının e-posta adresini yazın.
- **SMTP sunucusu**: "smtp_server" yerine SMTP sunucu adresini yazın (ör. Gmail için "smtp.gmail.com").
- **Dosya yolu**: "file_path" yerine eklemek istediğiniz dosyanın yolunu yazın.
- **E-posta konusu**: "message_subject" yerine istediğiniz konuyu yazın.
- **E-posta metni**: "MESSAGE_TEXT" yerine istediğiniz mesaj metnini yazın.

3. Gerekli kütüphaneleri yükleyin (eğer yüklü değilse):
    ```bash
    pip install python-dotenv  # Eğer yapılandırma için .env kullanıyorsanız
4. Betiği çalıştırın:
    ```bash
    python main.py
## Örnek Yapılandırma

Aşağıda yapılandırma örneğini görebilirsiniz:

    sender_email = "custom_sender@example.com"  # E-postayı göndermek istediğiniz adres
    receiver_email = "receiver_email@example.com"
    smtp_server = "smtp.gmail.com"
    filepath = "/path/to/your/file.txt"
    message["Subject"] = "Custom Email Test"
    text = """
    Merhaba,
    Bu Python betiği ile özelleştirilebilir bir gönderici adresi kullanarak gönderilen bir test e-postasıdır.
    """

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

## Güvenlik İpuçları
Hassas bilgileri doğrudan kodda sabitlemekten kaçının: E-posta kimlik bilgilerini saklamak için ortam değişkenlerini (.env) kullanın.
.env dosyasını .gitignore dosyasına ekleyerek hassas verilerin GitHub'a yüklenmesini önleyin.

---

# Customizable Email Sender

This Python script allows you to send emails with customizable sender and receiver addresses, along with attachments, using SMTP. It's a simple yet powerful way to automate email sending tasks.

## Features

- Customize sender and receiver email addresses.
- Send emails with a subject and body.
- Supports attachments (e.g., documents, images).
- Fully configurable SMTP settings.

## Setup and Usage

### Prerequisites

- Python 3.6 or higher
- Required libraries: `smtplib`, `ssl`, and `email` (these are standard in Python)

### Steps to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/customizable-email-sender.git
   cd customizable-email-sender
2. Open the script file and modify the following placeholders:
- **Sender email address**: Replace `"sender_mail"` with the email address you want to send the email from.
- **Receiver email address**: Replace `"reciver_mai"` with the recipient's email address.
- **SMTP server**: Replace `"smtp_server"` with the SMTP server address (e.g., `"smtp.gmail.com"` for Gmail).
- **File path**: Replace `"file_path"` with the path to the file you want to attach.
- **Email subject**: Replace `"message_subject"` with your desired subject.
- **Email body text**: Replace `"MESSAGE_TEXT"` with your desired message.
3. Install the required libraries if not already installed:

    ```bash
    pip install python-dotenv  # If you are using .env for configuration
4. Run the script:

    ```bash
    python main.py
## Example Configuration

Here’s an example of what your configuration might look like:
    
    ```bash
    sender_email = "custom_sender@example.com"  # The email address you want to send the email from
    receiver_email = "receiver_email@example.com"
    smtp_server = "smtp.gmail.com"
    filepath = "/path/to/your/file.txt"
    message["Subject"] = "Custom Email Test"
    text = """
    Hello,
    This is a test email sent from the Python script with a customizable sender.
    """
## Security Tips
Avoid hardcoding sensitive information: Use environment variables (.env) for storing email credentials.
Add .env to .gitignore to prevent sensitive data from being uploaded to GitHub.

## License
This project is licensed under the MIT License.