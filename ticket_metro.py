from datetime import datetime
from Exceptions import TicketError


class TicketAttributes:
    def __init__(self, price, origin=None, destination=None, expiration_date=None):
        self._price = price
        self._origin = origin
        self._destination = destination
        self._expiration_date = expiration_date
        self._purchase_date = datetime.now().strftime('%Y-%m-%d')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, new_exp_date):
        self._expiration_date = new_exp_date

    @property
    def purchase_date(self):
        return self._purchase_date


class Ticket:
    def __init__(self, attributes: TicketAttributes):
        self._attributes = attributes

    def update_attributes(self, attributes: TicketAttributes):
        self._attributes = attributes

    def as_dict(self):
        return {
            'price': self._attributes.price,
            'origin': self._attributes.origin,
            'destination': self._attributes.destination,
            'expiration_date': self._attributes.expiration_date,
            'purchase_date': self._attributes.purchase_date
        }

    def __str__(self):
        return f"{self.__class__.__name__} - {str(self.as_dict())}"


class SingleTripTicket(Ticket):
    def __init__(self, attributes: TicketAttributes):
        super().__init__(attributes)


class MultiStopTicket(Ticket):
    def __init__(self, attributes: TicketAttributes):
        if not isinstance(attributes, TicketAttributes):
            raise TicketError("Invalid attributes for MultiStopTicket.")
        super().__init__(attributes)

    def update_attributes(self, attributes: TicketAttributes):
        if not isinstance(attributes, TicketAttributes):
            raise TicketError("Invalid attributes for MultiStopTicket.")
        super().update_attributes(attributes)


class FlexibleTicket(Ticket):
    def __init__(self, attributes: TicketAttributes):
        if not isinstance(attributes, TicketAttributes):
            raise TicketError("Invalid attributes for FlexibleTicket.")
        super().__init__(attributes)

    def update_attributes(self, attributes: TicketAttributes):
        if not isinstance(attributes, TicketAttributes):
            raise TicketError("Invalid attributes for FlexibleTicket.")
        super().update_attributes(attributes)


class ShowTickets:
    def __init__(self):
        self.single_tickets = []
        self.multi_stop_tickets = []
        self.flexible_tickets = []

    def show_price(self, ticket):
        price_single_tickets = {}
        value_single_tickets = []
        values = ticket[1]
        price_single_tickets.update(values)
        for value in price_single_tickets.values():
            value_single_tickets.append(int(value))
            break
        price = value_single_tickets[0]
        return price

    def show_single_trip_ticket(self, price, origin, destination, date):
        single_ticket = [origin, {
            'price': price,
            'origin': origin,
            'destination': destination,
            'date': date
        }]
        self.single_tickets.extend(single_ticket)

    def show_multi_stop_ticket(self, price, origin, destination, date):
        multi_stop_ticket = [origin, {
            'price': price,
            'origin': origin,
            'destination': destination,
            'date': date
        }]
        self.multi_stop_tickets.extend(multi_stop_ticket)

    def show_flexible_ticket(self, price, origin, destination, date, expiration_date_input):
        flexible_ticket = [origin, {
            'price': price,
            'origin': origin,
            'destination': destination,
            'date': date,
            'expiration date': expiration_date_input
        }]
        self.flexible_tickets.extend(flexible_ticket)

