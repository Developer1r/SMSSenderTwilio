from twilio.rest import Client
import pandas

client = Client('API_KEY',
                'API_KEY')

# Read data from excel
excel_data = pandas.read_excel(
    'C:\\Users\\ASUS\\Desktop\\PythonProjects\\SMSSenderTwilio\\Check contacts.xlsx', sheet_name='Customers')

count = 0

# Iterate excel rows till to finish
for column in excel_data['Name'].tolist():
    # Assign customized message
    message = excel_data['Message'][0]

    # Format the message from excel sheet
    message = column + ", " + message + " = " + "https://th.bing.com/th/id/OIP.WtnU9WUh7x3E6z1MbalbnwHaE7?pid=ImgDet&rs=1",
    from_whatsapp_number = '+14439812068'
    to_whatsapp_number = '+972' + str(excel_data['Contact'][count])

    count = count + 1

    messageFinal = client.messages \
        .create(
            body=message,
            from_=from_whatsapp_number,
            to=to_whatsapp_number
        )

    print(to_whatsapp_number)
    print(messageFinal.sid)
