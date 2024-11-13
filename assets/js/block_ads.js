(function() {
    // Function to hide ads by detecting 'ds-ad' class or iframe sources related to ads
    function blockAds() {
        // Block 'ds-ad' elements (Disqus ad class)
        var adElements = document.querySelectorAll('.ds-ad');
        adElements.forEach(function(ad) {
            ad.style.display = 'none';  // Hide the ad element
        });

        // Block only ad-related iframes, not the Disqus comment iframe itself
        var iframes = document.querySelectorAll('iframe');
        iframes.forEach(function(iframe) {
            var iframeSrc = iframe.src || iframe.getAttribute('src');
            // Block iframes that load ads, but leave Disqus iframe visible
            if (iframeSrc && (iframeSrc.includes('disqus.com') && iframeSrc.includes('ads'))) {
                iframe.style.display = 'none';  // Hide the iframe if it's an ad
            }
        });
    }

    // Call the blockAds function when the page loads
    window.addEventListener('load', function() {
        blockAds();
    });

    // Additionally, periodically check for new ads if the page content changes dynamically
    setInterval(function() {
        blockAds();
    }, 1000);  // Check for ads every 1 second

    // Optional: stop the interval after 10 seconds (to prevent unnecessary checks)
    setTimeout(function() {
        clearInterval();
    }, 10000);  // Stop checking after 10 seconds
})();
