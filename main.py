import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Kullanıcının kendi gönderen e-posta adresini buraya yazması gerekiyor
sender_email = "sender_mail"  # Örn: "your_email@example.com"

# Kullanıcının alıcının e-posta adresini buraya yazması gerekiyor
receiver_email = "reciver_mai"  # Örn: "receiver_email@example.com"

message = MIMEMultipart("")
# Kullanıcının e-posta konusu için bir metin yazması gerekiyor
message["Subject"] = "message_subject"  # Örn: "This is a test email"
message["From"] = sender_email
message["To"] = receiver_email

# Kullanıcının e-posta metnini buraya yazması gerekiyor
text = """
MESSAGE_TEXT
"""  # Örn: "This is the email body text."

part1 = MIMEText(text, "plain")
message.attach(part1)

# Kullanıcının eklemek istediği dosyanın yolunu buraya yazması gerekiyor
filepath = "file_path"  # Örn: "/path/to/your/file.txt"

part2 = MIMEBase('application', "octet-stream")
part2.set_payload(open(filepath, "rb").read())
encoders.encode_base64(part2)

# Kullanıcının dosya adını değiştirebilmesi için
part2.add_header('Content-Disposition', 'attachment; filename="Document.docm"')
message.attach(part2)

# Kullanıcının SMTP sunucusunu ve portunu ayarlaması gerekiyor
context = ssl.create_default_context()
server = smtplib.SMTP("smtp_server", 587)  # Örn: "smtp.gmail.com"

server.starttls()
server.ehlo_or_helo_if_needed()

# E-posta gönderimi
server.sendmail(
    sender_email, receiver_email, message.as_string()
)
