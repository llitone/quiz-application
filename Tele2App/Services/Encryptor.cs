using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Tele2App.Services
{
    public static class Encryptor
    {
        public static string Encrypt(string password)
        {
            SHA512 sha = SHA512.Create();
            var result = sha.ComputeHash(Encoding.UTF8.GetBytes(password));
            return Convert.ToBase64String(result);
        }
    }
}
