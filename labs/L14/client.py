import humansize

def approximate_size(size):
    """Calls humansize approximate size with a default parameter of false"""
    return humansize.approximate_size(size, a_kilobyte_is_1024_bytes=False)

if __name__ == '__main__':
    print(approximate_size(1000000000000))
