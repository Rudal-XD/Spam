
if __name__ == "__main__":
  try:
    __import__("brute").main()
  except Exception as E:
    exit(str(E))
