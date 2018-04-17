using System;
using System.Collections.Generic;

namespace CreditToCustomerInterface
{
    class Program
    {
        static void Main(string[] args)
        {

            CardSlipParser p = new CardSlipParser();
            CtcApiHandler cah = new CtcApiHandler();

            string sampleOne = "MASTERCARD Auth Code: 759830 Merchant ID: 887 Account Number: ************3456 Expiry: 08/15 NO CARDHOLDER VERIFICATION";
            string sampleTwo = "Please debit my account Visa Debit 8768xxxxxxxx7682 Auth Code: 87ff6f";
            string sampleThree = "MASTERCARD Auth Code: 759830 Merchant ID: 887 Account Number: 5407********3456 Expiry: 15/08 NO CARDHOLDER VERIFICATION";

            Console.WriteLine("Sample card slip: ");
            Console.WriteLine(sampleOne);
            p.getCardDetails(sampleOne);

            foreach (KeyValuePair<string, string> kvp in p.getDetails())
            {
                Console.WriteLine("Key = {0}, Value = {1}", kvp.Key, kvp.Value);
            }

            p.clearDetails();

            Console.WriteLine("Sample card slip: ");
            Console.WriteLine(sampleThree);
            p.getCardDetails(sampleThree);

            foreach (KeyValuePair<string, string> kvp in p.getDetails())
            {
                Console.WriteLine("Key = {0}, Value = {1}", kvp.Key, kvp.Value);
            }

            Console.WriteLine(cah.GetCards(p.getDetails()));

        }
    }
}
