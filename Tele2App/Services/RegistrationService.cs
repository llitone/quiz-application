using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Json;
using System.Text;
using System.Threading.Tasks;
using Tele2App.Current;
using Tele2App.Model;

namespace Tele2App.Services
{
    public class RegistrationService
    {
        public async Task<bool> Registration(RegistrationUserModel model)
        {
            try
            {
                string endpoint = "http://127.0.0.1:1238/app/api/v1.0/users/";
                HttpClient client = new();
                JsonContent content = JsonContent.Create(model);

                var result = await client.PostAsync(endpoint, content);

                if (result.IsSuccessStatusCode)
                {
                    LoginService loginService = new();
                    await loginService.Login(model.PhoneNumber, model.Password);
                }

                return result.IsSuccessStatusCode;
            }
            catch
            {
                return false;
            }
        }
    }
}
