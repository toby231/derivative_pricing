from pricing.binomial_tree import onestep
from utils.option_properties import Option

def main():
    print("Initialising derivative pricing calculations")

    # Define option parameters

    option = Option(
        S_0 = 20,
        K = 21,
        T = 0.25,
        r = 0.12,
        sigma = 0.2
    )

    # Calculate price using one of many functions

    price = onestep(option)
    print(f"Calculated Option Price: {price:.2f}")
    return 

if __name__ == "__main__":
    main()