"""Task 4
Given a dictionary where marketing channels are keys and their conversion rates (as percentages) are values, find:

The marketing channel with the highest conversion rate.

The average conversion rate across all channels

marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}

# Expected Output:
# Best Performing Channel: Organic Search (5.6%)
# Average Conversion Rate: 4.0%"""

marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}

#The marketing channel with the highest conversion rate.
def highest_conv_rate(marketing_performance):
    highest_conv=max(marketing_performance,key=marketing_performance.get)
    print(f"\n 1) The marketing channel with the highest conversion rate is: {highest_conv}")

#The average conversion rate across all channels
def avg_conv_rate(marketing_performance):
    total_conversion=sum(marketing_performance.values())
    no_of_channels=len(marketing_performance)
    avg_conv=total_conversion/no_of_channels
    print(f"\n 2) The marketing channel with the average conversion rate is: {avg_conv}")

highest_conv_rate(marketing_performance)
avg_conv_rate(marketing_performance)