using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace CreditToCustomerInterface
{
    public class CardSlipParser
    {

        string[] cardTypes;
        Dictionary<string, string> details;
        Regex cardNumberRegex;
        Regex dateRegex;

        public CardSlipParser()
        {
            // Card Type
            // End date
            // Trailing Digits

            // Start Date
            // Leading Digits

            details = new Dictionary<string, string>();

            cardTypes = new string[] { "mastercard", "visa" };

            cardNumberRegex = new Regex(@"(\S{4})\S{8}(\S{4})");
            dateRegex = new Regex(@"(\d{2})\/(\d{2})");

        }

        public void getCardDetails(string cardSlip)
        {
            cardSlip = cardSlip.ToLower();

            // Find the cardType
            foreach (string s in cardTypes)
            {
                if (cardSlip.Contains(s))
                {
                    details.Add("cardType", s);
                    break;
                }
            }

            // Find the leading/trailing digits
            Match cardNumberMatch = cardNumberRegex.Match(cardSlip);
            details.Add("leadingDigits", cardNumberMatch.Groups[1].ToString());
            details.Add("trailingDigits", cardNumberMatch.Groups[2].ToString());

            // Find the end date
            Match endDateMatch = dateRegex.Match(cardSlip);
            //if (endDateMatch.S)
            if (!String.IsNullOrEmpty(endDateMatch.Groups[0].ToString()))
            {
                details.Add("endDate", endDateMatch.Groups[1].ToString() + endDateMatch.Groups[2].ToString());
            }
            else
            {
                details.Add("endDate", "0000");
            }

        }

        public Dictionary<string, string> getDetails()
        {
            return details;
        }

        public void clearDetails()
        {
            details.Clear();
        }
    }
}
