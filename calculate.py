"""
This program calculates the expected value (EV) for:
1. Repairing an old car
2. Buying a new car (which is safer)

It adds a factor for accident costs:
- Probability of a minor accident costing $5,000
- Probability of a major accident costing $500,000
The new car's safety features reduce these probabilities by x% and y%, respectively.

Then it compares them, printing the EV for both options.
"""

# -------------------------------------------------
# USER-SELECTED VARIABLES
# -------------------------------------------------

# -- Old Car Parameters --
REPAIR_COST = 2000.0             # R  (Cost to repair the old car)
PROB_RELIABLE = 0.5             # p  (Probability the repair holds up without major failure)
ADDITIONAL_MAINT_OLD = 2000.0     # M  (Additional/ongoing maintenance costs for the old car)
CATASTROPHIC_FAILURE_COST = 500.0  # F_cat (Cost/loss if the car fails catastrophically)
RESALE_OLD = 0              # V_old (Resale value of old car if it remains reliable)
INTANGIBLE_OLD = 0           # I_old (Stress, inconvenience, intangible cost of keeping old car)

# -- Accident Probabilities & Costs (Shared) --
MINOR_ACCIDENT_PROB = 0.50       # Probability of a minor accident in your timeframe
MAJOR_ACCIDENT_PROB = 0.01       # Probability of a major accident in your timeframe
COST_MINOR_ACCIDENT = 5000.0     # Cost of a minor accident
COST_MAJOR_ACCIDENT = 500000.0   # Cost of a major accident

# -- New Car Parameters --
PURCHASE_NEW = 35000.0           # P_new (Cost of the new car)
MAINT_NEW = 1500.0                # m (Expected maintenance for the new car)
RESALE_NEW = 18000.0             # V_new (Resale value of new car)
INTANGIBLE_NEW = 0          # I_new (Peace of mind, enjoyment, intangible benefit)

# -- Safety Reductions --
# These reduce the accident probabilities by a given fraction for the new car.
# For example, if SAFETY_REDUCTION_MINOR = 0.3, the minor accident probability drops by 30%.
SAFETY_REDUCTION_MINOR = 0.80    # x (30% reduction in chance of minor accident)
SAFETY_REDUCTION_MAJOR = 0.30    # y (50% reduction in chance of major accident)

# -------------------------------------------------
# CALCULATIONS
# -------------------------------------------------

# 1. Calculate expected accident cost for the old car
#    Probability * cost for minor + Probability * cost for major
accident_cost_old = (
    MINOR_ACCIDENT_PROB * COST_MINOR_ACCIDENT
    + MAJOR_ACCIDENT_PROB * COST_MAJOR_ACCIDENT
)

# 2. Calculate expected accident cost for the new car
#    The new car reduces the probabilities by SAFETY_REDUCTION_MINOR and SAFETY_REDUCTION_MAJOR.
#    So, "effective" probabilities become:
#      minor: MINOR_ACCIDENT_PROB * (1 - SAFETY_REDUCTION_MINOR)
#      major: MAJOR_ACCIDENT_PROB * (1 - SAFETY_REDUCTION_MAJOR)
accident_cost_new = (
    MINOR_ACCIDENT_PROB * (1 - SAFETY_REDUCTION_MINOR) * COST_MINOR_ACCIDENT
    + MAJOR_ACCIDENT_PROB * (1 - SAFETY_REDUCTION_MAJOR) * COST_MAJOR_ACCIDENT
)

# -------------------------------------------------
# EV of repairing the old car
# -------------------------------------------------
# Formula:
# EV(repair) = 
#   - REPAIR_COST 
#   - ADDITIONAL_MAINT_OLD 
#   - (1 - PROB_RELIABLE)*CATASTROPHIC_FAILURE_COST 
#   + PROB_RELIABLE*RESALE_OLD
#   - INTANGIBLE_OLD
#   - accident_cost_old   <-- new term for expected accident costs

# Break it into intermediate steps
repair_initial_outlay = -(REPAIR_COST + ADDITIONAL_MAINT_OLD)  # negative cost
repair_catastrophic = -(1 - PROB_RELIABLE) * CATASTROPHIC_FAILURE_COST
repair_resale = PROB_RELIABLE * RESALE_OLD
repair_intangibles = -INTANGIBLE_OLD
repair_accident = -accident_cost_old  # negative expected cost of accidents for old car

EV_repair = (   
    repair_initial_outlay
    + repair_catastrophic
    + repair_resale
    + repair_intangibles
    + repair_accident
)

# -------------------------------------------------
# EV of buying a new car
# -------------------------------------------------
# Formula:
# EV(new) = 
#   - PURCHASE_NEW 
#   - MAINT_NEW 
#   + RESALE_NEW 
#   + INTANGIBLE_NEW
#   - accident_cost_new   <-- new term for expected accident costs

new_initial_outlay = -(PURCHASE_NEW + MAINT_NEW)
new_resale = RESALE_NEW
new_intangibles = INTANGIBLE_NEW
new_accident = -accident_cost_new  # negative expected cost of accidents for new car

EV_new = (
    new_initial_outlay
    + new_resale
    + new_intangibles
    + new_accident
)

# -------------------------------------------------
# OUTPUT
# -------------------------------------------------
print("----- RESULTS -----")
print(f"EV of Repairing Old Car: {EV_repair:.2f}")
print(f"EV of Buying New Car:    {EV_new:.2f}")

# Compare:
# If EV_repair > EV_new, then repairing might be financially better.
# If EV_new > EV_repair, the new car might be the better option.
