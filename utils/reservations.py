from datetime import date, datetime
from typing import Union
from reservations.models import Reservation


def get_conflicted_reservations(
    reservation_in_date: Union[str, date],
    reservation_out_date: Union[str, date],
    reservation_id: str = "",
):

    available_reservations = Reservation.objects.all()

    # Converter o formato string para data
    # Pode facilitar a função de get room_categories quando informado datas específicas
    if not isinstance(reservation_in_date, date) or not isinstance(
        reservation_out_date, date
    ):
        try:
            if type(reservation_in_date) is str:
                reservation_in_date = datetime.strptime(
                    reservation_in_date, "%Y-%m-%d"
                ).date()
            if type(reservation_out_date) is str:
                reservation_out_date = datetime.strptime(
                    reservation_out_date, "%Y-%m-%d"
                ).date()
        except TypeError as error:
            raise TypeError(error)

    # Verificar se uma reservation_id foi informada ao chamar a função
    # Caso sim, deverá retornar os conflitos apenas das reservas que possuam id diferente ao reservation_id
    # Pode facilitar para a função de patch de reserva
    if reservation_id:
        available_reservations = [
            reservation
            for reservation in available_reservations
            if str(reservation.reservation_id) != reservation_id
        ]

    conflicted_reservations = []

    for reservation in available_reservations:

        if reservation.in_reservation_date <= reservation_in_date:
            if reservation.out_reservation_date >= reservation_in_date:
                conflicted_reservations.append(reservation)
        elif reservation.in_reservation_date >= reservation_in_date:
            if reservation.in_reservation_date <= reservation_out_date:
                conflicted_reservations.append(reservation)

    conflicted_reservations = [
        reservation
        for reservation in conflicted_reservations
        if reservation.status != "closed"
    ]

    return conflicted_reservations
