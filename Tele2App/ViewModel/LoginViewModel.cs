﻿using Tele2App.Model;
using Tele2App.Services;
using Tele2App.View;

namespace Tele2App.ViewModel
{
    public class LoginViewModel : BaseViewModel
    {
        private string _phoneNumber;
        private string _password;
        private LoginService _service;

        public LoginViewModel()
        {
            _service = new LoginService();
        }

        public string PhoneNumber
        {
            get { return _phoneNumber; }
            set
            {
                _phoneNumber = value;
                Notify(nameof(PhoneNumber));
            }
        }

        public string Password
        {
            get { return _password; }
            set
            {
                _password = value;
                Notify(nameof(Password));
            }
        }

        public ButtonCommand Registration
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    await Shell.Current.GoToAsync(nameof(RegistrationPage));
                });
            }
        }

        public ButtonCommand Login
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    LoginUserModel model = new()
                    {
                        PhoneNumber = _phoneNumber,
                        Password = Encryptor.Encrypt(_password)
                    };
                    var isCorrect = await _service.Login(model);
                    if(!isCorrect)
                        await Shell.Current.DisplayAlert("Ошибка", "Ошибка входа, попробуйте позже", "ОК");
                    else
                        await Shell.Current.GoToAsync(nameof(MainPage));
                });
            }
        }
    }
}