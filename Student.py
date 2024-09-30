from datetime import date
from enum import Enum

# Enums for Room Type, Payment Status, Gender, and Payment Method
class RoomType(Enum):
    SINGLE = "Single Room"
    DOUBLE = "Double Room"
    QUEEN = "Queen Room"
    KING = "King Room"
    SUITE = "Suite"

class PaymentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class PaymentMethod(Enum):
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    PAYPAL = "PayPal"
    CASH = "Cash"

# Guest class
class Guest:
    def __init__(self, first_name: str, last_name: str, email: str, phone: str, gender: Gender):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._gender = gender

    # Getter and Setter Methods
    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, first_name: str):
        self._first_name = first_name

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, last_name: str):
        self._last_name = last_name

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

    def get_phone(self) -> str:
        return self._phone

    def set_phone(self, phone: str):
        self._phone = phone

    def get_gender(self) -> Gender:
        return self._gender

    def set_gender(self, gender: Gender):
        self._gender = gender

# Reservation Class
class Reservation:
    def __init__(self, reservationID: str, guest: Guest, checkInDate: date, checkOutDate: date, roomType: RoomType, paymentStatus: PaymentStatus):
        self.reservationID = reservationID
        self.guest = guest
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.roomType = roomType
        self.paymentStatus = paymentStatus

    def get_reservation_id(self) -> str:
        return self.reservationID

    def set_reservation_id(self, reservationID: str):
        self.reservationID = reservationID

    def get_guest(self) -> Guest:
        return self.guest

    def set_guest(self, guest: Guest):
        self.guest = guest

    def get_check_in_date(self) -> date:
        return self.checkInDate

    def set_check_in_date(self, checkInDate: date):
        self.checkInDate = checkInDate

    def get_check_out_date(self) -> date:
        return self.checkOutDate

    def set_check_out_date(self, checkOutDate: date):
        self.checkOutDate = checkOutDate

    def get_room_type(self) -> RoomType:
        return self.roomType

    def set_room_type(self, roomType: RoomType):
        self.roomType = roomType

    def get_payment_status(self) -> PaymentStatus:
        return self.paymentStatus

    def set_payment_status(self, paymentStatus: PaymentStatus):
        self.paymentStatus = paymentStatus

# Payment Class
class Payment:
    def __init__(self, paymentID: str, reservation: Reservation, amount: float, paymentDate: date, paymentMethod: PaymentMethod, status: PaymentStatus):
        self.paymentID = paymentID
        self.reservation = reservation
        self.amount = amount
        self.paymentDate = paymentDate
        self.paymentMethod = paymentMethod
        self.status = status

    def get_payment_id(self) -> str:
        return self.paymentID

    def set_payment_id(self, paymentID: str):
        self.paymentID = paymentID

    def get_reservation(self) -> Reservation:
        return self.reservation

    def set_reservation(self, reservation: Reservation):
        self.reservation = reservation

    def get_amount(self) -> float:
        return self.amount

    def set_amount(self, amount: float):
        self.amount = amount

    def get_payment_date(self) -> date:
        return self.paymentDate

    def set_payment_date(self, paymentDate: date):
        self.paymentDate = paymentDate

    def get_payment_method(self) -> PaymentMethod:
        return self.paymentMethod

    def set_payment_method(self, paymentMethod: PaymentMethod):
        self.paymentMethod = paymentMethod

    def get_status(self) -> PaymentStatus:
        return self.status

    def set_status(self, status: PaymentStatus):
        self.status = status

# Staff class
class Staff:
    def __init__(self, staff_id: int, first_name: str, last_name: str, role: str, email: str):
        self._staff_id = staff_id
        self._first_name = first_name
        self._last_name = last_name
        self._role = role
        self._email = email

    # Getter and Setter Methods
    def get_staff_id(self) -> int:
        return self._staff_id

    def set_staff_id(self, staff_id: int):
        self._staff_id = staff_id

    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, first_name: str):
        self._first_name = first_name

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, last_name: str):
        self._last_name = last_name

    def get_role(self) -> str:
        return self._role

    def set_role(self, role: str):
        self._role = role

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

# Refund class
class Refund:
    def __init__(self, refund_id: int, payment: Payment, amount_refunded: float, refund_date: str):
        self._refund_id = refund_id
        self._payment = payment
        self._amount_refunded = amount_refunded
        self._refund_date = refund_date

    # Getter and Setter Methods
    def get_refund_id(self) -> int:
        return self._refund_id

    def set_refund_id(self, refund_id: int):
        self._refund_id = refund_id

    def get_payment(self) -> Payment:
        return self._payment

    def set_payment(self, payment: Payment):
        self._payment = payment

    def get_amount_refunded(self) -> float:
        return self._amount_refunded

    def set_amount_refunded(self, amount_refunded: float):
        self._amount_refunded = amount_refunded

    def get_refund_date(self) -> str:
        return self._refund_date

    def set_refund_date(self, refund_date: str):
        self._refund_date = refund_date

# Creating Objects

# Creating a guest
guest = Guest("Ted", "Vera", "ledvera@mac.com", "505-661-1110", Gender.MALE)

# Creating a reservation
reservation = Reservation("52523687", guest, date(2010, 8, 22), date(2010, 8, 24), RoomType.QUEEN, PaymentStatus.PENDING)

# Creating a payment
payment = Payment("15541050358", reservation, 201.48, date(2024, 9, 30), PaymentMethod.CREDIT_CARD, PaymentStatus.COMPLETED)

# Creating staff
staff = Staff(1, "Sara", "Ali", "Receptionist", "receptionist@example.com")

# Creating a refund
refund = Refund(1, payment, 0.0, "N/A")  # No refund in this scenario

# Displaying Information
print(f"Guest: {guest.get_first_name()} {guest.get_last_name()}, Email: {guest.get_email()}, Phone: {guest.get_phone()}")
print(f"Reservation ID: {reservation.get_reservation_id()}, Check-in: {reservation.get_check_in_date()}, Check-out: {reservation.get_check_out_date()}, Room Type: {reservation.get_room_type().value}")
print(f"Payment ID: {payment.get_payment_id()}, Amount: ${payment.get_amount()}, Status: {payment.get_status().value}")
print(f"Staff: {staff.get_first_name()} {staff.get_last_name()}, Role: {staff.get_role()}")
print(f"Refund ID: {refund.get_refund_id()}, Amount Refunded: ${refund.get_amount_refunded()}, Refund Date: {refund.get_refund_date()}")