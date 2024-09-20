amount_to_convert = 500

nz_to_aus_rate = 0.95
nz_dollars = amount_to_convert

aus__dollars = nz_dollars * nz_to_aus_rate
print(aus__dollars)

aus__dollars = amount_to_convert
nz_dollars = aus__dollars / nz_to_aus_rate
print(nz_dollars)