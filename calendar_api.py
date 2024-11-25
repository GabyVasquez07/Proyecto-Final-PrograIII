from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
from google.auth.transport.requests import Request

#Este ámbito nos permite el acceso a la API
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Esta función añade el evento a Google Calendar
def add_event_to_calendar(tipo_pago, correo_destino, monto_pago, fecha_vencimiento, diaDrecordatorio):
    creds = None

    # El archivo token.json almacena los tokens de acceso y actualización del usuario, y es
    # creado automáticamente cuando el flujo de autorización se completa por primera vez.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Si no tenemos credenciales válidas, dejamos que el flujo de autorización se maneje
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Guardar las credenciales para la próxima vez
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Conexión a la API de Google Calendar
    service = build('calendar', 'v3', credentials=creds)

    # Crear el evento con los datos que se reciben como parámetros
    event = {
        'summary': f'Recordatorio de pago: {tipo_pago}',
        'location': 'El Salvador',  
        'description': f'Recordatorio para el pago de {monto_pago} en fecha de vencimiento {fecha_vencimiento}',
        'start': {
            'dateTime': diaDrecordatorio,  # Este debe ser un string en formato ISO 8601
            'timeZone': 'America/El_Salvador',  
        },
        'end': {
            'dateTime': diaDrecordatorio,  
            'timeZone': 'America/El_Salvador',
        },
        'attendees': [
            {'email': correo_destino},  # Correo del destinatario
        ],
        'reminders': {
            'useDefault': True,  # Usar recordatorios predeterminados
        },
    }

    # Llamada a la API para crear el evento
    try:
        event_result = service.events().insert(
            calendarId='primary', 
            body=event
        ).execute()

        print(f"Evento creado: {event_result.get('htmlLink')}")
    except Exception as e:
        print(f"Ocurrió un error al crear el evento: {e}")
