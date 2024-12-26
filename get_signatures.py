# Given a pageCount, representing the number of pages
# in an input PDF,
# 
# Returns a "sigature guide" for a PDF arranged into folios and signatures.
# This "guide" is an array of items, each item representing a signature.
# Each item is an integer, representing the number of pages that should
# be in that specific signature.
#
# If the provided pageCount is not evenly divisible by 4, we cannot
# produce a suitable set of signatures, so we return None.
def getSignatures(pageCount):
  # pageCount must be evenly divisible by 4
  if (pageCount % 4 != 0):
    return None
  # Handle some cases with small page counts.
  # We handle up to 52, which makes it easier to reason about
  # our fallback case later. Showing the rough pattern we're using
  # feels like it might be helpful as well, the cases for 28 and onwards
  # felt like a good visualization to me.
  if pageCount == 4: return [4]
  if pageCount == 8: return [8]
  if pageCount == 12: return [12]
  if pageCount == 16: return [16]
  if pageCount == 20: return [12, 8]
  if pageCount == 24: return [12, 12]
  if pageCount == 28: return [16, 12]
  if pageCount == 32: return [16, 16]
  if pageCount == 36: return [12, 12, 12]
  if pageCount == 40: return [16, 12, 12]
  if pageCount == 44: return [16, 16, 12]
  if pageCount == 48: return [16, 16, 16]
  if pageCount == 52: return [16, 12, 12, 12]
  # Remaining cases will need an array to add to
  signatures = []
  # Our ideal case is a pageCount divisible by 16.
  # To handle all other cases, we use signatures of 12 to account for
  # the remainder pages. We know that our page count is 52 or greater,
  # this factors in to our mod16 == 4 case.
  mod16 = pageCount % 16
  if mod16 == 12:
    # Note this only works if pageCount is >= 28
    for i in range((pageCount - 12) // 16):
      signatures.append(16)
    signatures.append(12)
    return signatures
  elif mod16 == 8:
    # Note this only works if pageCount is >= 40
    for i in range((pageCount - 24) // 16):
      signatures.append(16)
    signatures.append(12)
    signatures.append(12)
    return signatures
  elif mod16 == 4:
    # Note this only works if pageCount >= 52
    for i in range((pageCount - 36) // 16):
      signatures.append(16)
    signatures.append(12)
    signatures.append(12)
    signatures.append(12)
    return signatures
  # Base case, mod16 is zero
  for i in range(pageCount // 16):
    signatures.append(16)
  return signatures