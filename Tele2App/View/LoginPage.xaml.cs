﻿using Tele2App.ViewModel;

namespace Tele2App.View;

public partial class LoginPage : ContentPage
{

	public LoginPage()
	{
		InitializeComponent();
	}

    protected override bool OnBackButtonPressed()
    {
        return true;
    }
}

