from clockwork import clockwork

api = clockwork.API( '05cf0deeaa97a4fb5751ddcfb46889b1f15b3d0c' )

def send_time_message( number, event, time ) :
    """
    This will send a message with the time registered
    """
    # Message variable
    message = clockwork.SMS(
        to = number,
        message = ( "Tú tiempo ha sido {0}, puedes checar los detalles en http://actime.mx/event/rd/{1}. ¡Gracias por competir con Actime!" ).format( time, event.pk )
    )
    # get the response    
    response = api.send(message)
    # validate if the response is successful
    if response.success:
        print (response.id)
        return True
    else:
        print ( response.error_code )
        print ( response.error_message )
        return False
    # End of validations
# End of send_time_messsage function