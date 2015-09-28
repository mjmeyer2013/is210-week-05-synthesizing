#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" week 5 assignment"""

import datetime

CURDATE = None


def get_current_date():
    """Get current datatime from datetime module.

    Function will return current date time when called.

    Args:
        get_date(mix): measurment of datetime module
    Returns:
        date(int): Current date and time from measurment
    Example:
        >>> get_current_date()
        datetime.date(2015, 9, 28)
    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
