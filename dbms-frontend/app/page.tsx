'use client'
import React,{use, useEffect,useState} from 'react';
import { Link } from "@nextui-org/link";
import { Snippet } from "@nextui-org/snippet";
import { Code } from "@nextui-org/code"
import { button as buttonStyles } from "@nextui-org/theme";
import { siteConfig } from "@/config/site";
import { title, subtitle } from "@/components/primitives";
import { GithubIcon } from "@/components/icons";
import LinearGraph from '@/components/LinearGraph';
import axios from 'axios';


export default function Home() {

	interface Cart {
		Cart_id: string;
		User_id: string;
		Item_id: string;
		Quantity: number;
		Added_data: Date;
		Updated_data: Date;
		Deleted_data: Date;
		Active: boolean;
		sub_total: number;
	}
	
	interface Catalog {
		item_id: string;
		item_name: string;
		price: number;
		manufacturer_id: string;
		Category_id: string;
		Quantity: number;
		Added_data: Date;
		Updated_data: Date;
		Deleted_data: Date;
		Discount: number;
		Description: string;
		Weight: number;
		Dimension_id: string;
		image_url: string;
		Rating: number[];
		Reviews: string[];
		Tags: string[];
	}
	
	interface Checkout {
		User_ID: string;
		Cart_ID?: string;
		Payment_ID?: string;
		Added_date?: Date;
		Shipping_ID?: string;
		Shipping_Cost: number;
		Total_Paid: number;
		Complete: boolean;
	}
	
	interface Customer {
		name: string;
		age: number;
		phone_number: string;
		email: string;
		gender: string;
		date_of_birth: Date;
		account_creation_date: Date;
		address_id: string;
		total_purchase_cost: number;
	}
	
	interface LoginAccess {
		Login_id: string;
		User_id: string;
		Login_time: Date;
		Logout_time: Date;
		IP_address: string;
		Device_type: string;
	}
	
	interface Address {
		Address_ID: string;
		Line1: string;
		Line2?: string;
		City: string;
		State: string;
		Country: string;
		PinCode: string;
	}
	
	interface Manufacturer {
		Manufacturer_ID: string;
		Manufacturer_Name: string;
		Location: string;
		GSTIN: string;
	}
	
	interface Category {
		Category_ID: string;
		Name: string;
	}
	
	interface Dimension {
		Dimension_ID: string;
		Length: number;
		Breadth: number;
		Height: number;
	}
	
	interface Payment {
		User_ID: string;
		Amount: number;
		Method_Payment: string;
		Date_of_txn: Date;
		Transaction_Status: string;
		Payment_Status: string;
		Confirmation_Number: string;
	}
	
	interface Shipping {
		User_ID: string;
		Amount: number;
		Method_Payment: string;
		Date_of_txn: Date;
		Transaction_Status: string;
		Payment_Status: string;
		Confirmation_Number: string;
	}
	
	// Function to split attributes into different lists
	function splitAttributes<T, K extends keyof T>(data: T[], key: K): T[K][] {
		return data.map(item => item[key]);
	}
	

	const base_url = "https://dbms-ap.onrender.com/api"  

	const [dimensions, setDimensions] = useState()
	const [manufacturers, setManufacturers] = useState()
	const [categories, setCategories] = useState()
	const [customers, setCustomers] = useState()
	const [loginAccesses, setLoginAccesses] = useState()
	const [addresses, setAddresses] = useState()
	const [catlogs, setCatlogs] = useState()
	const [payments, setPayments] = useState()
	const [carts, setCarts] = useState()
	const [checkouts, setCheckouts] = useState()
	const [shippings, setShippings] = useState()
	const [items, setItems] = useState()

	useEffect(() => {
		const endpoints = [
			"/dimensions",
			"/manufacturers",
			"/categories",
			"/customers",
			"/login-accesses",
			"/addresses",
			"/catlogs",
			"/payments",
			"/carts",
			"/checkouts",
			"/shippings",
			"/items",
		]
		endpoints.forEach(endpoint => {
			axios.get(base_url + endpoint)
			.then(res => {
				console.log(res.data)
				switch (endpoint) {
					case "/dimensions":
						setDimensions(res.data)

						break
					case "/manufacturers":
						setManufacturers(res.data)

						break
					case "/categories":
						setCategories(res.data)

						break
					case "/customers":
						setCustomers(res.data)

						break
					case "/login-accesses":
						setLoginAccesses(res.data)

						break
					case "/addresses":
						setAddresses(res.data)

						break
					case "/catlogs":
						setCatlogs(res.data)

						break
					case "/payments":
						setPayments(res.data)

						break
					case "/carts":
						setCarts(res.data)

						break
					case "/checkouts":
						setCheckouts(res.data)

						break
					case "/shippings":
						setShippings(res.data)

						break
					case "/items":
						setItems(res.data)

						break
				}
			})
			.catch(err => {
				console.log(err)
			})
		})
	}
	, [ ])

	
	// Splitting attributes for Cart
	const cartIds: string[] = splitAttributes(carts || [], 'Cart_id');
	const userIds: string[] = splitAttributes(carts || [], 'User_id');
	const itemIds: string[] = splitAttributes(carts || [], 'Item_id');
	const quantities: number[] = splitAttributes(carts || [], 'Quantity');
	const addedDates: Date[] = splitAttributes(carts || [], 'Added_data');
	const updatedDates: Date[] = splitAttributes(carts || [], 'Updated_data');
	const deletedDates: Date[] = splitAttributes(carts || [], 'Deleted_data');
	const actives: boolean[] = splitAttributes(carts || [], 'Active');
	const subTotals: number[] = splitAttributes(carts || [], 'sub_total');


	
	// Splitting attributes for Catalog
	const catalogItemIds: string[] = splitAttributes(catlogs || [], 'item_id');
	const catalogItemNames: string[] = splitAttributes(catlogs || [], 'item_name');
	const catalogPrices: number[] = splitAttributes(catlogs || [], 'price');
	const catalogManufacturerIds: string[] = splitAttributes(catlogs || [], 'manufacturer_id');
	const catalogCategoryIds: string[] = splitAttributes(catlogs || [], 'Category_id');
	const catalogQuantities: number[] = splitAttributes(catlogs || [], 'Quantity');
	const catalogAddedDates: Date[] = splitAttributes(catlogs || [], 'Added_data');
	const catalogUpdatedDates: Date[] = splitAttributes(catlogs || [], 'Updated_data');
	const catalogDeletedDates: Date[] = splitAttributes(catlogs || [], 'Deleted_data');
	const catalogDiscounts: number[] = splitAttributes(catlogs || [], 'Discount');
	const catalogDescriptions: string[] = splitAttributes(catlogs || [], 'Description');
	const catalogWeights: number[] = splitAttributes(catlogs || [], 'Weight');
	const catalogDimensionIds: string[] = splitAttributes(catlogs || [], 'Dimension_id');
	const catalogImageUrls: string[] = splitAttributes(catlogs || [], 'image_url');
	const catalogRatings: number[][] = splitAttributes(catlogs || [], 'Rating');
	const catalogReviews: string[][] = splitAttributes(catlogs || [], 'Reviews');


	//Splitting attributes for Checkout
	const checkoutUserIds: string[] = splitAttributes(checkouts || [], 'User_ID');
	const checkoutCartIds: string[] = splitAttributes(checkouts || [], 'Cart_ID');
	const checkoutPaymentIds: string[] = splitAttributes(checkouts || [], 'Payment_ID');
	const checkoutAddedDates: Date[] = splitAttributes(checkouts || [], 'Added_date');
	const checkoutShippingIds: string[] = splitAttributes(checkouts || [], 'Shipping_ID');
	const checkoutShippingCosts: number[] = splitAttributes(checkouts || [], 'Shipping_Cost');
	const checkoutTotalPaids: number[] = splitAttributes(checkouts || [], 'Total_Paid');
	const checkoutCompletes: boolean[] = splitAttributes(checkouts || [], 'Complete');

	// Splitting attributes for Customer
	const customerNames: string[] = splitAttributes(customers || [], 'name');
	const customerAges: number[] = splitAttributes(customers || [], 'age');
	const customerPhoneNumbers: string[] = splitAttributes(customers || [], 'phone_number');
	const customerEmails: string[] = splitAttributes(customers || [], 'email');
	const customerGenders: string[] = splitAttributes(customers || [], 'gender');
	const customerDatesOfBirth: Date[] = splitAttributes(customers || [], 'date_of_birth');
	const customerAccountCreationDates: Date[] = splitAttributes(customers || [], 'account_creation_date');
	const customerAddressIds: string[] = splitAttributes(customers || [], 'address_id');
	const customerTotalPurchaseCosts: number[] = splitAttributes(customers || [], 'total_purchase_cost');

	// Splitting attributes for LoginAccess
	const loginAccessLoginIds: string[] = splitAttributes(loginAccesses || [], 'Login_id');
	const loginAccessUserIds: string[] = splitAttributes(loginAccesses || [], 'User_id');
	const loginAccessLoginTimes: Date[] = splitAttributes(loginAccesses || [], 'Login_time');
	const loginAccessLogoutTimes: Date[] = splitAttributes(loginAccesses || [], 'Logout_time');
	const loginAccessIPAddresses: string[] = splitAttributes(loginAccesses || [], 'IP_address');
	const loginAccessDeviceTypes: string[] = splitAttributes(loginAccesses || [], 'Device_type');

	// Splitting attributes for Address
	const addressIds: string[] = splitAttributes(addresses || [], 'Address_ID');
	const addressLine1s: string[] = splitAttributes(addresses || [], 'Line1');
	const addressLine2s: string[] = splitAttributes(addresses || [], 'Line2');
	const addressCities: string[] = splitAttributes(addresses || [], 'City');
	const addressStates: string[] = splitAttributes(addresses || [], 'State');
	const addressCountries: string[] = splitAttributes(addresses || [], 'Country');
	const addressPinCodes: string[] = splitAttributes(addresses || [], 'PinCode');

	// Splitting attributes for Manufacturer
	const manufacturerIds: string[] = splitAttributes(manufacturers || [], 'Manufacturer_ID');
	const manufacturerNames: string[] = splitAttributes(manufacturers || [], 'Manufacturer_Name');
	const manufacturerLocations: string[] = splitAttributes(manufacturers || [], 'Location');
	const manufacturerGSTINs: string[] = splitAttributes(manufacturers || [], 'GSTIN');

	// Splitting attributes for Category
	const categoryIds: string[] = splitAttributes(categories || [], 'Category_ID');
	const categoryNames: string[] = splitAttributes(categories || [], 'Name');

	// Splitting attributes for Dimension
	const dimensionIds: string[] = splitAttributes(dimensions || [], 'Dimension_ID');
	const dimensionLengths: number[] = splitAttributes(dimensions || [], 'Length');
	const dimensionBreadths: number[] = splitAttributes(dimensions || [], 'Breadth');
	const dimensionHeights: number[] = splitAttributes(dimensions || [], 'Height');

	// Splitting attributes for Payment
	const paymentUserIds: string[] = splitAttributes(payments || [], 'User_ID');
	const paymentAmounts: number[] = splitAttributes(payments || [], 'Amount');
	const paymentMethodPayments: string[] = splitAttributes(payments || [], 'Method_Payment');
	const paymentDatesOfTxn: Date[] = splitAttributes(payments || [], 'Date_of_txn');
	const paymentTransactionStatuses: string[] = splitAttributes(payments || [], 'Transaction_Status');
	const paymentPaymentStatuses: string[] = splitAttributes(payments || [], 'Payment_Status');
	const paymentConfirmationNumbers: string[] = splitAttributes(payments || [], 'Confirmation_Number');

	// Splitting attributes for Shipping
	const shippingUserIds: string[] = splitAttributes(shippings || [], 'User_ID');
	const shippingAmounts: number[] = splitAttributes(shippings || [], 'Amount');
	const shippingMethodPayments: string[] = splitAttributes(shippings || [], 'Method_Payment');
	const shippingDatesOfTxn: Date[] = splitAttributes(shippings || [], 'Date_of_txn');
	const shippingTransactionStatuses: string[] = splitAttributes(shippings || [], 'Transaction_Status');
	const shippingPaymentStatuses: string[] = splitAttributes(shippings || [], 'Payment_Status');
	const shippingConfirmationNumbers: string[] = splitAttributes(shippings || [], 'Confirmation_Number');




	return (
		<section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">
			<div className="inline-block h-1/2 text-center justify-center p-5">
				<h1 className={title()}>View E-Commerce Analytics from data stored in </h1>
				<h1 className={title({ color: "violet" })}> MongoDB and ExpressJS &nbsp;</h1>
				<br />
			</div>
			<div>
				{/* customer age to total cost */}
				<LinearGraph titleString="Age to Spending Comparison" xLables={customerAges} xaxisnums={customerAges} data={customerTotalPurchaseCosts} />
				{/*  */}
				<LinearGraph 
				titleString="Sales Trends Over Time" 
				xLables={addedDates} 
				xaxisnums={addedDates} 
				data={subTotals} />

			{/* <LinearGraph 
			titleString="Product Price Trends Over Time" 
			xLables={catalogAddedDates} 
			xaxisnums={catalogAddedDates} 
			data={catalogPrices} 
			/> */}
			{/* <LinearGraph 
			titleString="Customer Purchase History" 
			xLables={customerAges.map(age => age.toString())} 
			xaxisnums={customerAges} 
			data={customerTotalPurchaseCosts} 
			/> */}
			{/* <LinearGraph 
			titleString="Login Access Frequency" 
			xLables={loginAccessLoginTimes.map(time => time.toISOString())} 
			xaxisnums={loginAccessLoginTimes} 
			data={Array.from({ length: loginAccessLoginTimes.length }, (_, i) => i + 1)} 
			/> */}
			{/* <LinearGraph 
			titleString="Manufacturer Sales Performance" 
			xLables={addedDates} 
			xaxisnums={addedDates.filter((_, i) => manufacturerIds[i] === 'desired_manufacturer_id')} 
			data={subTotals.filter((_, i) => manufacturerIds[i] === 'desired_manufacturer_id')} 
			/> */}
			{/* <LinearGraph 
			titleString="Category-wise Sales Comparison" 
			xLables={categoryNames} 
			xaxisnums={categoryIds} 
			data={subTotals} 
			/> */}
			{/* <LinearGraph 
			titleString="Product Ratings Over Time" 
			xLables={catalogAddedDates} 
			xaxisnums={catalogAddedDates} 
			data={catalogRatings.map(ratings => ratings.reduce((acc, rating) => acc + rating, 0) / ratings.length)} 
			/> */}
			{/* <LinearGraph 
			titleString="Shipping Costs Over Time" 
			xLables={shippingDatesOfTxn} 
			xaxisnums={shippingDatesOfTxn} 
			data={shippingAmounts} 
			/> */}


			</div>
		</section>
	);
}
