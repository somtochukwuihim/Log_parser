# Guide to plan creation for Activation Team. 

### If  one of Antenatal \ Obstetrics is (covered),
Edit these;

1. New born
1. Surgery
1. Fertility
1. Spa
1. Cancer
1. Antenatal
1. Demise
1. Neonatal (don't edit)
1. Gym
1. Dental
1. Renal/dialysis
1. Physiotherapy care

### Note
 
`If obste is showing 777.77 it means new born antenatal and neonatal will be covered. Antenatal will be covered for global limited(unlimited)`
 
`If obste shows any figure like 250,000.00 all three, new born, antenatal(will be covered for the shown amount) and neonatal will be covered too.`


********************************************************************************
### if both Antenatal and Obstetrics is NOT (covered)
Edit these;

1. Surgery
1. Fertility
1. Spa
1. Cancer
1. Demise
1. Gym
1. Dental
1. Renal/dialysis
1. Physiotherapy care.

### Note 
`For when obstetrics isn't covered.(0.00 yearly)`

### If a client is been moved to an SME status from a Corporate status
When a clients previous plan is confirmed to not be an SME plan and when editing their family plan,
ensure to use the SME Benefit Table to fill the;
* routine new born.
* antenatal
* neonatal.
* and demise if the plan is not a red beryl.


## Pseudo-Code for deciphering antenatal/Obstetrics coverage

antenatal --- ante  | obstetrics -- obste
 
if ante == 'covered' and obste is '0.00':
ante(newborn, antenatal, neonatal) will be covered
 
If ante == 'Not covered' and obste is '777.77':
ante(newborn, antenatal, neonatal) will be covered
 
if ante == 'Not covered' and obste is '0.00':
ante(newborn, antenatal, neonatal) will not be covered
 
if ante == 'covered' or 'Any figure seen' and obste  == 'any figure seen':
ante(newborn, antenatal, neonatal) will not be covered. Only antenatal will be covered for 'that figure seen'

Thanks for reading.