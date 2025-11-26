import random

def simulate_zkp(trials=20, knows_password=True):
    success_count = 0

    for i in range(trials):
        path_entered = random.choice(['A', 'B'])  # alice picks path
        challenge = random.choice(['A', 'B'])  # bob asks for a path

        if knows_password:
            success = True  # can always get thru door
        else:
            success = path_entered == challenge  # gotta guess right

        if success:
            success_count += 1
            
    return success_count, trials


def calculate_malicious_probability(trials=20, simulations=10000):
    # runs it a bunch of times to see how often attacker gets lucky
    
    # (1/2)^20 basically
    theoretical_prob = (0.5) ** trials
    
    # run it a bunch to check
    full_success_count = 0
    
    for _ in range(simulations):
        successes, total = simulate_zkp(trials=trials, knows_password=False)
        if successes == total:  # fooled Bob completely
            full_success_count += 1
    
    empirical_prob = full_success_count / simulations
    
    return theoretical_prob, empirical_prob


if __name__ == "__main__":
    print("=" * 50)
    print("ZKP - Ali Baba Cave")
    print("=" * 50)
    
    # honest prover
    print("\n--- knows password ---")
    successes, total = simulate_zkp(trials=20, knows_password=True)
    print(f"success: {successes}/{total}")
    
    # attacker guessing
    print("\n--- doesnt know password (guessing) ---")
    successes, total = simulate_zkp(trials=20, knows_password=False)
    print(f"success: {successes}/{total}")
    
    # probability calc
    print("\n--- probability stuff ---")
    theoretical, empirical = calculate_malicious_probability(trials=20, simulations=10000)
    
    print(f"theoretical prob: {theoretical:.10f}")
    print(f"thats like 1 in {int(1/theoretical):,}")
    print(f"empirical (10k runs): {empirical:.10f}")
    
    print("\nbasically impossible to fake over 20 rounds")

