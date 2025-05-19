
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node 
        else:
            current = self.head 
            while current.next:
                current = current.next 
            current.next = new_node

    def delete(self):
        if not self.head:
            print("No node to delete!")
        elif not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")
        
ll = LinkedList() 
# Append values to the list
ll.append(10)   # List: 10
ll.append(20)   # List: 10 -> 20
ll.append(30)   # List: 10 -> 20 -> 30
ll.append(40)   # List: 10 -> 20 -> 30 -> 40
ll.delete()
# Display the current list
ll.display()     # Output: 10 -> 20 -> 30 -> 40 -> None



    public function calculatePremium($targetFutureValue, $annualInterestRate, $paymentMonths, $growthYears, $paymentMode)
    {

        $monthlyInterestRate    = $annualInterestRate / 12;
        $quarterlyInterestRate  = $annualInterestRate / 4;
        $semiAnnualInterestRate = $annualInterestRate / 2;

        switch ($paymentMode) {
            case "monthly":
                $compoundingFactor = pow(1 + $monthlyInterestRate, $paymentMonths) - 1;
                $compoundedGrowth  = pow(1 + $annualInterestRate, $growthYears);
                break;
            case "quarterly":
                $compoundingFactor = pow(1 + $quarterlyInterestRate, $paymentMonths / 3) - 1;
                $compoundedGrowth  = pow(1 + $annualInterestRate, $growthYears);
                break;
            case "semi-annually":
                $compoundingFactor = pow(1 + $semiAnnualInterestRate, $paymentMonths / 6) - 1;
                $compoundedGrowth  = pow(1 + $annualInterestRate, $growthYears);
                break;
            default:
                return "Invalid Payment Mode";
        }

        $requiredSavings = $targetFutureValue / $compoundedGrowth;

        if ($compoundingFactor == 0) {
            return "Invalid calculation parameters.";
        }

        $requiredSavingsPerPeriod = $requiredSavings * $monthlyInterestRate / $compoundingFactor;

        $requiredMonthlyPremium = $requiredSavingsPerPeriod / 0.85;

        return number_format($requiredMonthlyPremium, 2);
    }