using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Http;

namespace CreditToCustomerInterface
{
    public class CtcApiHandler
    {

        static HttpClient client;

        public CtcApiHandler()
        {
            client = new HttpClient();
        }

        public string GetCards(Dictionary<string, string> details)
        {
            // https://anthonyobrien-dot-yreceipts-dev.appspot.com/test?leadingDigits=5407&trailingDigits=3456&startDate=1208&endDate=1508&cardType=mastercard

            string address = "https://anthonyobrien-dot-yreceipts-dev.appspot.com/test";
            string query = String.Format("?leadingDigits={0}&trailingDigits={1}&startDate={2}&endDate={3}&cardType={4}", 
                                         details["leadingDigits"], 
                                         details["trailingDigits"], 
                                         1208, 
                                         details["endDate"],
                                         details["cardType"]
                                        );

            string url = address + query;
            return Get(url);
        }

        private string Get(string url)
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.AutomaticDecompression = DecompressionMethods.GZip | DecompressionMethods.Deflate;

            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            using (Stream stream = response.GetResponseStream())
            using (StreamReader reader = new StreamReader(stream))
            {
                return reader.ReadToEnd();
            }
        }
    }
}
