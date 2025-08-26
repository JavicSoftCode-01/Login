"""
Utility functions for input validation and security in the login system.
Following OOP principles:
- Encapsulation: Private methods and clear interfaces
- Inheritance: BaseValidator class
- Polymorphism: Different validation strategies
- Abstraction: High-level validation interface
"""
import re
from typing import Tuple, Optional
from abc import ABC, abstractmethod


class BaseValidator(ABC):
  """Abstract base class for validators following the Strategy pattern."""

  @abstractmethod
  def validate(self, value: str) -> Tuple[bool, Optional[str]]:
    """Validate a value and return result and error message if any."""
    pass


class EmailValidator(BaseValidator):
  """Email validation strategy."""

  def __init__(self):
    self.max_length = 50
    self._email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

  def validate(self, email: str) -> Tuple[bool, Optional[str]]:
    """
    Validate email format and constraints.
    Returns: (is_valid, error_message)
    """
    if not email:
      return False, "El correo electrónico es requerido."

    if len(email) > self.max_length:
      return False, f"El correo electrónico no puede exceder {self.max_length} caracteres."

    if ' ' in email:
      return False, "El correo electrónico no puede contener espacios."

    if any(ord(char) > 127 for char in email):
      return False, "El correo electrónico no puede contener emojis o caracteres especiales."

    if not re.match(self._email_pattern, email):
      return False, "Formato de correo electrónico inválido."

    return True, None


class PasswordValidator(BaseValidator):
  """Password validation strategy."""

  def __init__(self):
    self.min_length = 8
    self.max_length = 20

  def validate(self, password: str) -> Tuple[bool, Optional[str]]:
    """
    Validate password constraints.
    Returns: (is_valid, error_message)
    """
    if not password:
      return False, "La contraseña es requerida."

    if len(password) < self.min_length:
      return False, f"La contraseña debe tener al menos {self.min_length} caracteres."

    if len(password) > self.max_length:
      return False, f"La contraseña no puede exceder {self.max_length} caracteres."

    return True, None


class InputValidator:
  """Main validator class using composition of validation strategies."""

  def __init__(self):
    self._email_validator = EmailValidator()
    self._password_validator = PasswordValidator()

  def validate_login_input(self, email: str, password: str) -> Tuple[bool, Optional[str]]:
    """
    Validate both email and password.
    Returns: (is_valid, error_message)
    """
    # Validate email
    is_valid, error = self._email_validator.validate(email)
    if not is_valid:
      return False, error

    # Validate password
    is_valid, error = self._password_validator.validate(password)
    if not is_valid:
      return False, error

    return True, None
