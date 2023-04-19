using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tele2App.Model;

namespace Tele2App.Current
{
    public class CurrentUser
    {
        private static CurrentUser _user = new ();

        private CurrentUser() { }
        public int Id { get; set; }
        public string Name { get; set; }
        public string PhoneNumber { get; set; }
        public int Points { get; set; }

        public static CurrentUser GetUser()
        {
            return _user;
        }

        public static void Login(LoginUserModel user)
        {
            _user.Id = user.Id;
            _user.Name = user.Name;
            _user.PhoneNumber = user.PhoneNumber;
            _user.Points = user.Points;
        }

        public static void Logout()
        {
            _user.Id = 0;
            _user.Name = string.Empty;
            _user.PhoneNumber = string.Empty;
            _user.Points = 0;
        }
    }
}
