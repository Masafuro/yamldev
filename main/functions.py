from tqdm import tqdm

def add(params):
    """
    サンプル関数:
    入力のリスト内の数値を合計します。
    """
    return sum(params)



from decimal import Decimal, getcontext

def calculate_pi(digits):
    """
    Calculate the value of pi to the specified number of digits.

    Args:
        digits (int): The number of decimal places to calculate pi.

    Returns:
        str: The value of pi to the specified number of digits as a string.
    """
    # 型チェックを追加
    digits = int(digits[0])

    if not isinstance(digits, int):
        raise TypeError("The number of digits must be an integer.")
    
    if digits < 1:
        raise ValueError("The number of digits must be greater than 0.")

    # Set precision for decimal calculations
    getcontext().prec = digits + 2  # Add extra precision to ensure accuracy

    # Using the Gauss-Legendre algorithm for pi calculation
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    for _ in tqdm(range(10)):  # Iterates 10 times for high precision
        next_a = (a + b) / 2
        next_b = (a * b).sqrt()
        next_t = t - p * (a - next_a) ** 2
        a, b, t, p = next_a, next_b, next_t, 2 * p

    pi = (a + b) ** 2 / (4 * t)

    # Convert pi to string with the specified precision
    return str(pi)[:digits + 2]  # Include "3." part

from datetime import datetime, timedelta



def get_datetime_with_offset(offset_hours):
    """
    Get the current date and time adjusted for a given timezone offset.

    Args:
        offset_hours (int or float): The timezone offset in hours (e.g., +9 for JST, -5 for EST).

    Returns:
        str: The current date and time in ISO 8601 format adjusted for the timezone offset.
    """
    offset_hours = float(offset_hours[0])

    if not isinstance(offset_hours, (int, float)):
        raise TypeError("The offset_hours must be an integer or float.")
    
    # 現在のUTC日時を取得
    utc_now = datetime.utcnow()
    
    # タイムゾーンオフセットを適用
    adjusted_time = utc_now + timedelta(hours=offset_hours)
    
    # ISO 8601形式で日時を文字列として返す
    return adjusted_time.isoformat()