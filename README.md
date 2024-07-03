# Streamlit_TestDashboard
## Problem Statement and Requirements

Make a solution that solves the following problem.

A company sells hundreds of products on-line and people place orders from all over the world, just like eBay. Each item has a different weight and price.

And each order can be a combination of different numbers of items. Now each of these orders are to be put into different packages and sent to the courier company for delivery.
But there are certain rules while splitting items into packages, they are as below:

> 1. If the cost of all the items in an order is more than $250, split those items into multiple packages, otherwise one package would be enough.

> 2. If the items in the same order are split into multiple packages, then the weight of the packages should be equally distributed over the packages to save courier charges.

> 3. While splitting, NO PACKAGE can have a total price equal or above $250

Create a page which has the following:

> 1. A simple vertical list of items (in the format Name - price - weight), with a check box next to item

> 2. A button saying "Place order"

When the user clicks on **"Place order"**, the selected items should be submitted to the same page without refreshing the page and the above splitting rules should be applied to divide this particular
order into multiple packages, and display the output result on the same page. Below is a sample
output on how it should look like:

>This order has following packages:

>Package 1
>
>Items - Item 1, Item 3, item 7
>
>Total weight - 510g
>
>Total price - $240
>
>Courier price - $15


>Package 2
>
>Items - Item 4, Item 6, item 2
>
>Total weight - 530g
>
>Total price - $160
>
>Courier price - $15

*Note: Items and courier prices are in the Test_info.xls attached, The code should be split between UI and
backend. The application will be marked based on the specifically comments (where required), formatting,
naming conventions, functionality, modularity, coding standard, the approach taken to reduce lines of codes
and best practice/approach/plugins taken on both frontend and backend.*


## Packaging Rules and Mathematical Model

### Objective and Constraints

Minimize the number of packages $\( n \)$ and the variance in weight among these packages to achieve relatively equal weight distribution.

#### Constraints:
1. **Price Constraint**:
   - Ensure that the total cost of items in any package is less than $250:
   
     $$\sum_{i_k \in p_j} c_k < 250 \quad \forall p_j \in P$$

   Where  $\( c_k \)$  is the cost of item $\( i_k \).$
   

3. **Full Distribution**:
   - Every item must be in exactly one package, and no item is in more than one package:

     $$\bigcup_{j=1}^{n} p_j = I \quad \text{and} \quad p_j \cap p_k = \emptyset \text{ for } j \neq k$$
   
   Where $\( I \)$ is the set of all items and $\( P \)$ is the set of all packages.

4. **Weight Distribution**:
   - Aim to minimize the variance in weights among packages. Let $\( W_j \)$ be the total weight of package $\( p_j \)$:

     $$W_j = \sum_{i_k \in p_j} w_k$$
     
   - Minimize the variance in weights:

     $$\text{Var}(W) = \frac{1}{n} \sum_{j=1}^{n} (W_j - \bar{W})^2$$
     
   Where $\( \bar{W} = \frac{1}{n} \sum_{j=1}^{n} W_j \)$ is the average weight of the packages. <br/>

## Algorithm Pipeline

![image](https://github.com/wanasyraf4/Streamlit_TestDashboard/assets/107595740/fe203fbb-3581-4434-8fa0-b0a680dbccc2)


**Step 1: Initialization** <br/>
Load Items: Gather all items into a list where each item has properties: name, price, and weight. <br/>
Prepare Containers: Initialize an empty list to hold packages. <br/>

**Step 2: Preprocessing** <br/>
Sort Items: Sort items by price in descending order to optimize package cost efficiency.

Step 3: Package Formation** <br/>
- Initialize Temporary Storage:
Start with an empty temporary package and set its accumulated cost and weight to zero.<br/>

- Iterate Over Items:
For each item, check if adding the item to the current package would keep the total cost of the package below $250.
>If yes, add the item to the current package.
>If no, finalize the current package and start a new one. <br/>

**Step 4: Price and Weight Balancing**<br>
- Calculate Average Weight:
After all items are assigned to initial packages, calculate the average weight of these packages.<br/>
- Adjust Packages:
Iterate through the packages, redistributing items between packages where necessary to minimize the difference between each package’s weight and the average weight, ensuring that no package's cost exceeds $250. <br/>

**Step 5: Finalization**<br>
Complete Packaging:
Ensure all items are placed in a package.
Check for any last adjustments needed to balance weights without violating cost constraints.

**Step 6: Output Result**<br>
Return or Display Packages:
Output the list of packages, each with its list of items, total price, and total weight.
