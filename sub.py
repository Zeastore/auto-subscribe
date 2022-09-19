function doPreProcessing($x)
{
	if($subscriptionButtons[$x].dataset.isSubscribed === undefined || $subscriptionButtons[$x].dataset.isSubscribed === false)
	{
		$newSubscriptions.push($subscriptionButtons[$x]);
		console.log("#" + ($x+1) + " of " + $subscriptionButtons.length + " will be subscriped to.");
	}
	else
	{
		console.log("Skipping #" + ($x+1) + " of " + $subscriptionButtons.length + ", already subscribed.");
	}
}

function doSubscription($x, $delay)
{
	setTimeout(function()
	{ 
		$newSubscriptions[$x].click();
		console.log("Subscribed to #" + ($x+1) + " of " + $newSubscriptions.length);

		if($x == ($newSubscriptions.length-1))
		{
			console.log("Script finished.");
			console.log("All channels should be subscribed to, it is advised that you scroll down and check the last subscription button to verify this. YouTube starts blocking subscription requests when it detects them as 'fake', which could happen with this script. If that happens, run the script again after a few hours and it should continue where it ended last time.")
		}

	}, $delay);
}

// Select subscription buttons
$subscriptionButtons = document.getElementsByClassName("yt-uix-subscription-button");
$newSubscriptions = [];

// Pre-process found buttons
for(var $x = 0; $x < $subscriptionButtons.length; $x++)
{
	doPreProcessing($x);
}

$delay = 0;

// Subscribe to channels
for(var $x = 0; $x < $newSubscriptions.length; $x++)
{
	console.log("\n\nWe will now subscribe to " + $newSubscriptions.length + " channels.");

	$delay += (3000 * Math.random());
	doSubscription($x, $delay);
}
